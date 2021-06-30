import sys
from bignum.utils import ops

def _add(a,b,c,r):
    min_len = min(len(a),len(b))
    base = 2 ** r
    carry = 0
    for i in range(min_len):
        uv = a[i] + b[i] + carry
        
        u,v = ops.divmod_sp(uv,2**r,r)
        c[i] = v
        carry = u
    
    i += 1
    if i == len(a) and i == len(b):
        c[i] = carry
    elif i == len(a):
        c[i:] = b[i:]
        c[i] += carry
    elif i == len(b):
        c[i:] = a[i:]
        c[i] += carry
        
    return c


def cal(A,B,r):
    A_rev = A[::-1]
    B_rev = B[::-1]
    max_len = max(len(A),len(B))
    C_rev = [0] * (max_len + 1)
    base = 2 ** r

    # main procedure
    C_rev = _add(A_rev, B_rev, C_rev, r)
    C = C_rev[::-1]

    print(f'Addition res: {C} base {base}')
    return C

if __name__=='__main__':
    a = [8,7]
    b = [8,7]
    r = 4
    res = cal(a,b,r)
    
