#!/usr/bin/env python3
"""Compact, directed prime-log prefixes with constant-time endpoint queries.

One uint64 stores primality of 64 consecutive odd integers. All primes in
that word receive the same lower log(word start) and upper log(word end)
weight, directed onto a 2**(-24) grid. Two uint64 prefixes and two uint32
word weights give 32 bytes per 128 integers, or about 2.5 GB at 10**10.

The small endpoint range uses the existing finer PrimeLogIntervals prefix.
An interval crossing its cutoff is split there. In particular, a LOWER
prefix is subtracted only from the SAME lower prefix; it is never used as
an upper estimate. Returned interval sums use the existing 2**(-32) grid
and Python integers, so conversion cannot overflow uint64.

Sieving, packing, logarithm buckets, weights, prefix sums, masks, and all
queries use integer arithmetic. The inherited log lookup table was built
with directed mpmath intervals. No floating-point logarithm is evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
import time

import numpy as np

from erdos_699_bft_prime_bootstrap import PrimeLogIntervals, SCALE, BUCKETS

NATIVE_SCALE = 1 << 24
TO_EXISTING_SCALE = SCALE // NATIVE_SCALE
assert TO_EXISTING_SCALE == 256


def _digest(array):
    return hashlib.sha256(memoryview(array).cast('B')).hexdigest()


class CompactPrimeLogIntervals:
    """Exact sieve with directed compact weights, for limits through 10**10.

    `base` remains available for proper-prime-power construction. Its prime
    arrays cover base.limit, not this object's larger limit; deliberately
    do not expose them under misleading `primes`/`prefix_lo` attributes.
    """
    def __init__(self, limit=10**10, *, base=None, base_limit=10**8,
                 chunk_words=1 << 20):
        start = time.monotonic()
        self.limit = int(limit)
        assert 128 <= self.limit <= 10**10
        assert chunk_words > 0
        self.base = base if base is not None else PrimeLogIntervals(min(base_limit,self.limit))
        self.base_limit = self.base.limit
        assert 2 <= self.base_limit <= self.limit
        self.timings = {'base_seconds':time.monotonic()-start}
        phase = time.monotonic()
        odd_count = (self.limit+1)//2
        sieve = np.ones(odd_count,dtype=np.bool_)
        sieve[0] = False
        for p in range(3,isqrt(self.limit)+1,2):
            if sieve[p//2]:
                sieve[(p*p)//2::p] = False
        self.timings['sieve_seconds'] = time.monotonic()-phase
        phase = time.monotonic()
        packed = np.packbits(sieve,bitorder='little')
        del sieve
        word_count = (odd_count+63)//64
        if packed.size != word_count*8:
            packed = np.pad(packed,(0,word_count*8-packed.size))
        self.words = packed.view('<u8')
        assert self.words.flags.c_contiguous
        self.timings['packing_seconds'] = time.monotonic()-phase
        self.word_count = word_count
        self.lower_weight = np.empty(word_count,dtype=np.uint32)
        self.upper_weight = np.empty(word_count,dtype=np.uint32)
        self.lower_prefix = np.empty(word_count+1,dtype=np.uint64)
        self.upper_prefix = np.empty(word_count+1,dtype=np.uint64)
        self.lower_prefix[0] = self.upper_prefix[0] = 0
        self._lo_table = self.base.log_lo//TO_EXISTING_SCALE
        self._hi_table = (self.base.log_hi+TO_EXISTING_SCALE-1)//TO_EXISTING_SCALE
        self._log2_lo = self.base.log2_lo//TO_EXISTING_SCALE
        self._log2_hi = (self.base.log2_hi+TO_EXISTING_SCALE-1)//TO_EXISTING_SCALE
        self._powers = np.array([1 << b for b in range(self.limit.bit_length()+2)],dtype=np.int64)
        assert odd_count*int(self._log_bounds(np.array([128*word_count-1],dtype=np.int64),True)[0]) < 2**64
        phase = time.monotonic()
        odd_prime_count = 0
        for first in range(0,word_count,chunk_words):
            last = min(word_count,first+chunk_words)
            starts = 128*np.arange(first,last,dtype=np.int64)+1
            low = self._log_bounds(starts,False)
            high = self._log_bounds(starts+126,True)
            assert int(high.max()) < 2**32
            self.lower_weight[first:last] = low
            self.upper_weight[first:last] = high
            counts = np.bitwise_count(self.words[first:last]).astype(np.uint64)
            odd_prime_count += int(np.sum(counts,dtype=np.uint64))
            self.lower_prefix[first+1:last+1] = self.lower_prefix[first]+np.cumsum(counts*low,dtype=np.uint64)
            self.upper_prefix[first+1:last+1] = self.upper_prefix[first]+np.cumsum(counts*high,dtype=np.uint64)
        self.timings['weights_and_prefixes_seconds'] = time.monotonic()-phase
        self.prime_count = odd_prime_count+1  # The packed array contains odd primes only.
        self._compact_at_base_lo = self._native_prefix(self.base_limit,False)
        self._compact_at_base_hi = self._native_prefix(self.base_limit,True)
        self._base_at_cut = int(np.searchsorted(self.base.primes,self.base_limit,side='right'))
        phase = time.monotonic()
        self.metadata = {
            'algorithm':'odd-word-directed-prefix-v1','sieve_limit':self.limit,
            'base_sieve_limit':self.base_limit,'word_count':word_count,
            'prime_count':self.prime_count,'native_fixed_point_scale':NATIVE_SCALE,
            'returned_fixed_point_scale':SCALE,'integers_per_word':128,
            'retained_compact_bytes':sum(a.nbytes for a in (self.words,self.lower_weight,self.upper_weight,self.lower_prefix,self.upper_prefix)),
            'prime_word_sha256':_digest(self.words),
            'lower_weight_sha256':_digest(self.lower_weight),'upper_weight_sha256':_digest(self.upper_weight),
            'lower_prefix_sha256':_digest(self.lower_prefix),'upper_prefix_sha256':_digest(self.upper_prefix),
            'base_prime_log_certificate':self.base.metadata,
        }
        self.timings['hash_seconds'] = time.monotonic()-phase
        self.timings['total_seconds'] = time.monotonic()-start

    def save(self, directory):
        """Persist checked native arrays for shared read-only mmap reuse."""
        directory = Path(directory)
        directory.mkdir(parents=True,exist_ok=True)
        for name in ('words','lower_weight','upper_weight','lower_prefix','upper_prefix'):
            np.save(directory/(name+'.npy'),getattr(self,name),allow_pickle=False)
        (directory/'metadata.json').write_text(json.dumps(self.metadata,indent=2)+'\n')

    @classmethod
    def load(cls, directory, *, base=None):
        """Load mmap arrays, checking their hashes and inherited base prefix."""
        directory = Path(directory)
        metadata = json.loads((directory/'metadata.json').read_text())
        assert metadata['algorithm'] == 'odd-word-directed-prefix-v1'
        obj = cls.__new__(cls)
        obj.metadata = metadata
        obj.limit = metadata['sieve_limit']
        obj.base_limit = metadata['base_sieve_limit']
        obj.word_count = metadata['word_count']
        obj.prime_count = metadata['prime_count']
        obj.base = base if base is not None else PrimeLogIntervals(obj.base_limit)
        assert obj.base.metadata == metadata['base_prime_log_certificate']
        names = {'words':'prime_word_sha256','lower_weight':'lower_weight_sha256',
                 'upper_weight':'upper_weight_sha256','lower_prefix':'lower_prefix_sha256',
                 'upper_prefix':'upper_prefix_sha256'}
        for name,key in names.items():
            array = np.load(directory/(name+'.npy'),mmap_mode='r',allow_pickle=False)
            assert _digest(array) == metadata[key]
            setattr(obj,name,array)
        obj._compact_at_base_lo = obj._native_prefix(obj.base_limit,False)
        obj._compact_at_base_hi = obj._native_prefix(obj.base_limit,True)
        obj._base_at_cut = int(np.searchsorted(obj.base.primes,obj.base_limit,side='right'))
        obj.timings = {}
        return obj

    def _log_bounds(self, values, upper):
        """Directed native-grid bounds using exact binary mantissa buckets."""
        exponents = np.searchsorted(self._powers,values,side='right')-1
        offsets = ((values << 14) >> exponents)-BUCKETS
        assert np.all((offsets>=0)&(offsets<BUCKETS))
        if upper:
            return exponents.astype(np.uint64)*self._log2_hi+self._hi_table[offsets+1]
        return exponents.astype(np.uint64)*self._log2_lo+self._lo_table[offsets]

    def _native_prefix(self, endpoints, upper=False):
        """Weighted sum over packed odd primes <= each integer endpoint."""
        original = np.asarray(endpoints,dtype=np.int64)
        xs = original.reshape(-1)
        assert np.all((xs>=0)&(xs<=self.limit))
        odd_numbers = (xs+1)//2
        word_indices, bits = odd_numbers//64, odd_numbers%64
        prefix = self.upper_prefix if upper else self.lower_prefix
        weights = self.upper_weight if upper else self.lower_weight
        result = prefix[word_indices].copy()
        partial = bits != 0
        if np.any(partial):
            indices = word_indices[partial]
            masks = np.left_shift(np.uint64(1),bits[partial].astype(np.uint64))-np.uint64(1)
            counts = np.bitwise_count(self.words[indices]&masks).astype(np.uint64)
            result[partial] += counts*weights[indices]
        result = result.reshape(original.shape)
        return int(result) if original.ndim == 0 else result

    def interval_sum_lower(self, uppers, lowers):
        """Lower log sum over disjoint (lower,upper] intervals, in SCALE units."""
        u,v = np.asarray(uppers,dtype=np.int64),np.asarray(lowers,dtype=np.int64)
        assert u.shape == v.shape and u.ndim == 1
        keep = u>v
        u,v = u[keep],v[keep]
        if not len(u):return 0
        assert np.all(v>=0) and np.all(u<=self.limit)
        assert np.all(u[1:]<=v[:-1])
        below = np.minimum(u,self.base_limit)
        low_part = below>v
        iu = np.searchsorted(self.base.primes,below[low_part],side='right')
        il = np.searchsorted(self.base.primes,v[low_part],side='right')
        total = int(np.sum(self.base.prefix_lo[iu]-self.base.prefix_lo[il],dtype=np.uint64))
        high_part = u>self.base_limit
        if np.any(high_part):
            high_u = self._native_prefix(u[high_part])
            high_v = self._native_prefix(np.maximum(v[high_part],self.base_limit))
            total += int(np.sum(high_u-high_v,dtype=np.uint64))*TO_EXISTING_SCALE
        return total

    def theta_upper_integer(self, endpoints):
        """Integer ceil upper bound for theta(x), scalar or integer array."""
        original = np.asarray(endpoints,dtype=np.int64)
        xs = original.reshape(-1)
        assert np.all((xs>=0)&(xs<=self.limit))
        answer = np.empty(xs.size,dtype=np.int64)
        small = xs<=self.base_limit
        ii = np.searchsorted(self.base.primes,xs[small],side='right')
        answer[small] = ((self.base.prefix_hi[ii]+SCALE-1)//SCALE).astype(np.int64)
        if np.any(~small):
            weights = self._native_prefix(xs[~small],True)-self._compact_at_base_hi
            base_units = (int(self.base.prefix_hi[self._base_at_cut])+TO_EXISTING_SCALE-1)//TO_EXISTING_SCALE
            weights += np.uint64(base_units)
            answer[~small] = ((weights+NATIVE_SCALE-1)//NATIVE_SCALE).astype(np.int64)
        answer = answer.reshape(original.shape)
        return int(answer) if original.ndim == 0 else answer

    def count_primes(self,endpoints):
        """Exact prime-count query, used to validate word packing and masks."""
        original = np.asarray(endpoints,dtype=np.int64)
        xs = original.reshape(-1)
        assert np.all((xs>=0)&(xs<=self.limit))
        # Counts are not retained, so this diagnostic is deliberately linear.
        results=[]
        for x in xs:
            n=(int(x)+1)//2;word,bits=divmod(n,64)
            count=int(np.sum(np.bitwise_count(self.words[:word]),dtype=np.uint64))
            if bits:count+=(int(self.words[word])&((1<<bits)-1)).bit_count()
            results.append(count+int(x>=2))
        answer=np.array(results,dtype=np.int64).reshape(original.shape)
        return int(answer) if original.ndim==0 else answer


def validate_small(compact):
    """Independent full prime array at <=10**8 checks all word weights."""
    assert compact.limit<=10**8
    reference=PrimeLogIntervals(compact.limit)
    assert compact.prime_count==len(reference.primes)
    for first in range(1,len(reference.primes),1<<20):
        last=min(len(reference.primes),first+(1<<20))
        ps=reference.primes[first:last]
        words=(ps//2)//64
        assert np.all(compact.lower_weight[words].astype(np.uint64)*TO_EXISTING_SCALE <= reference.prefix_lo[first+1:last+1]-reference.prefix_lo[first:last])
        assert np.all(compact.upper_weight[words].astype(np.uint64)*TO_EXISTING_SCALE >= reference.prefix_hi[first+1:last+1]-reference.prefix_hi[first:last])
    rng=np.random.default_rng(699)
    endpoints=np.r_[0,1,2,3,127,128,129,compact.base_limit,compact.limit,rng.integers(0,compact.limit+1,2000)]
    assert np.all(compact.count_primes(endpoints)==np.searchsorted(reference.primes,endpoints,side='right'))
    exact_upper=(reference.prefix_hi[np.searchsorted(reference.primes,endpoints,side='right')]+SCALE-1)//SCALE
    assert np.all(compact.theta_upper_integer(endpoints)>=exact_upper)
    points=np.unique(np.r_[0,compact.limit,rng.integers(0,compact.limit+1,4000)])
    u,v=points[1:][::-1],points[:-1][::-1]
    old=reference.interval_sum_lower(u,v)
    new=compact.interval_sum_lower(u,v)
    assert new<=old and new>0
    return {'all_prime_weights_checked':len(reference.primes)-1,
            'prime_count_queries_checked':len(endpoints),'disjoint_intervals_checked':len(u),
            'relative_lower_weight_loss':float((old-new)/old)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit',type=int,default=10**8)
    parser.add_argument('--base-limit',type=int,default=10**6)
    parser.add_argument('--validate',action='store_true')
    parser.add_argument('--output')
    parser.add_argument('--cache-dir')
    parser.add_argument('--load-cache')
    args=parser.parse_args()
    compact=(CompactPrimeLogIntervals.load(args.load_cache) if args.load_cache else
             CompactPrimeLogIntervals(args.limit,base_limit=args.base_limit))
    if args.cache_dir:compact.save(args.cache_dir)
    result={'metadata':compact.metadata,'timings':compact.timings}
    if args.validate:result['validation']=validate_small(compact)
    # A representative decreasing family of 2,000 disjoint intervals.
    points=np.linspace(compact.base_limit,compact.limit,4001,dtype=np.int64)
    u,v=points[1::2][::-1],points[::2][:-1][::-1]
    start=time.monotonic()
    for _ in range(1000):compact.interval_sum_lower(u,v)
    result['queries_2000_intervals_per_second']=1000/(time.monotonic()-start)
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
