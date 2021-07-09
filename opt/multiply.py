import sys
import time
from bignum.utils import ops

def _mul(a,b,c,r,ub):
    base = 2 ** (r-ub)
    carry = 0
    for i in range(len(c)-1):
        tmp = 0
        for j in range(i+1):
            if j >= len(b) or i-j >= len(a):
                continue
            x1 = b[j][0]
            x2 = a[i-j][0]
            prod = ops.mul(x1,x2)
            tmp = ops.add(tmp,prod)
        uv = tmp + carry
        u,v = ops.divmod_sp(uv,base,r-ub)
        c[i] = v
        carry = u
    c[i+1] += carry
    return c

# Multi-precision CM algorithm
# input: 
#   A = [a_n, a_n-1, ..., a_0]
#   B = [b_m, b_m-1, ..., b_0]
#   r base
# output:
#   C = [c_n+m+1, ..., c_0]
def cal(A,B,args):
    A_rev = A[::-1]
    B_rev = B[::-1]
    C_rev = [0] * (len(A) + len(B))
    r = args.r
    ub = args.ub
    base = 2 ** (r - ub)
   
    # main procedure
    #t1 = time.process_time()
    C_rev = _mul(A_rev,B_rev,C_rev,r,ub)
    #t2 = time.process_time()
    #print('cpu time:',t2-t1)
    C = C_rev[::-1]

    print(f'CM res: {C} base {base}')
    return C

if __name__=='__main__':
    a = [[2, '-1'], [0, '-1'], [7, '-1']] # 1000 0111
    b = [[2, '-1'], [0, '-1'], [7, '-1']] # 1000 0111
    r = 4
    res = cal(a,b,r)
