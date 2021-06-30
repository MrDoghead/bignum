import sys
from bignum.utils import ops

# input: a,b,c are list of base r digits
# output: reversed and updated list C
def _mul(a,b,c,r):
    base = 2 ** r
    for i in range(len(b)):
        carry = 0
        for j in range(len(a)):
            uv = c[i+j] + a[j] * b[i] + carry

            u,v = ops.divmod_sp(uv,base,r)
            #u = uv // (2 ** r)
            #v = uv % (2 ** r)
            c[i+j] = v
            carry = u
        c[i+j+1] = u
    return c

# Multi-precision CM algorithm
# input: 
#   A = [a_n, a_n-1, ..., a_0]
#   B = [b_m, b_m-1, ..., b_0]
#   r base
# output:
#   C = [c_n+m+1, ..., c_0]
def cal(A,B,r):
    A_rev = A[::-1]
    B_rev = B[::-1]
    C_rev = [0] * (len(A) + len(B) + 1)
    base = 2 ** r
   
    # main procedure
    C_rev = _mul(A_rev,B_rev,C_rev,r)
    C = C_rev[::-1]

    print(f'CM res: {C} base {base}')
    return C

if __name__=='__main__':
    a = [8, 7] # 1000 0111
    b = [8, 7] # 1000 0111
    r = 4
    res = cal(a,b,r)
