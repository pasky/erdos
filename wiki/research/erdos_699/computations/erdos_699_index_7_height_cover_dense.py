#!/usr/bin/env python3
"""Exact dense lookup for the existing directed lower theta prefix.

This changes only lookup time. At every integer x<=limit, dense[x] equals
prefix_lo[searchsorted(primes,x,side='right')], with no new rounding.
The optional binary cache is outside the repository and checked by hashes.
"""
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
import os
import fcntl

import numpy as np

from erdos_699_index_7_gcd_pointwise import PointwiseGcdLower,sharp_prime_sum_lower


def ensure_dense_lower_prefix(theta,directory=None):
    directory=Path(directory or Path(__file__).resolve().parents[4]/'tmp'/'erdos699'/f'prime-prefix-{theta.limit}')
    directory.mkdir(parents=True,exist_ok=True)
    path=directory/'dense_lower.u64'
    meta_path=directory/'dense_lower.json'
    with (directory/'dense_build.lock').open('a+b')as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        built=False
        if not meta_path.exists():
            temporary=directory/f'dense_lower.{os.getpid()}.tmp'
            dense=np.memmap(temporary,dtype=np.uint64,mode='w+',shape=(theta.limit+1,))
            # A newly truncated/extended file has zero-filled unwritten bytes.
            dense[theta.primes]=theta.prefix_lo[1:]
            np.maximum.accumulate(dense,out=dense)
            assert int(dense[0])==0 and int(dense[-1])==int(theta.prefix_lo[-1])
            dense.flush()
            metadata={'limit':theta.limit,'dtype':'uint64','entries':theta.limit+1,
                      'source_prime_array_sha256':theta.metadata['prime_array_sha256'],
                      'source_lower_prefix_sha256':theta.metadata['lower_prefix_sha256'],
                      'dense_array_sha256':sha256(memoryview(dense)).hexdigest(),
                      'construction':'Zero array, source lower prefix at prime positions, then exact in-place maximum accumulation.'}
            del dense
            temporary.replace(path)
            temp_meta=directory/f'dense_lower.{os.getpid()}.json'
            temp_meta.write_text(json.dumps(metadata,indent=2)+'\n')
            temp_meta.replace(meta_path)
            built=True
        metadata=json.loads(meta_path.read_text())
        assert metadata['limit']==theta.limit and metadata['entries']==theta.limit+1
        assert metadata['source_prime_array_sha256']==theta.metadata['prime_array_sha256']
        assert metadata['source_lower_prefix_sha256']==theta.metadata['lower_prefix_sha256']
        assert path.stat().st_size==8*(theta.limit+1)
        dense=np.memmap(path,dtype=np.uint64,mode='r',shape=(theta.limit+1,))
        if not built:assert sha256(memoryview(dense)).hexdigest()==metadata['dense_array_sha256']
        dense.flags.writeable=False
    return dense,metadata


def dense_prime_sum_lower(theta,dense,uppers,lowers):
    keep=uppers>lowers
    uppers,lowers=uppers[keep],lowers[keep]
    if not len(uppers):return 0
    assert np.all(uppers[1:]<=lowers[:-1])
    exact=uppers<=theta.limit
    total=int(np.sum(dense[uppers[exact]]-dense[lowers[exact]],dtype=np.uint64))
    if np.any(~exact):
        total+=sharp_prime_sum_lower(theta,uppers[~exact],lowers[~exact])
    return total


class DensePointwiseGcdLower(PointwiseGcdLower):
    def __init__(self,theta,directions,*,dense,terms=4000,powers=None):
        self.dense=dense
        assert len(dense)==theta.limit+1 and dense.dtype==np.uint64
        super().__init__(theta,directions,terms=terms,powers=powers)

    @lru_cache(maxsize=512)
    def log_lower(self,m):
        A,B,C=self.directions
        H=A+B+C
        assert isinstance(m,int) and m>=1 and B*m>=2 and H*m<2**62
        uppers=(H*m-1)//self.ts
        lowers=np.maximum.reduce(((A*m+1)//self.den[:,0],B*m//self.den[:,1],(C*m+1)//self.den[:,2]))
        return (dense_prime_sum_lower(self.theta,self.dense,uppers,lowers)
                +self.powers.interval_sum_lower(uppers,lowers))


if __name__=='__main__':
    from erdos_699_index_7_height_cover_cache import ensure_prime_prefix
    theta,directory=ensure_prime_prefix()
    dense,metadata=ensure_dense_lower_prefix(theta,directory)
    print(json.dumps({'directory':str(directory),'metadata':metadata},indent=2))
