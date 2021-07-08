import sys
import time
from bignum.utils import ops

'''
# input: a,b,c are list of base r digits
# output: reversed and updated list C
def _mul(a,b,c,r):
    base = 2 ** (r-1)
    for i in range(len(b)):
        carry = 0
        for j in range(len(a)):
            product = ops.int_mul(a[j][:-1],b[i][:-1])
            sum1 = ops.add(c[i+j], product)
            sum2 = ops.add(sum1, carry)
            uv = sum2
            u,v = ops.divmod_sp(uv,base,r)
            c[i+j] = v
            carry = u
        c[i+j+1] = u
    return c
'''

def _mul(a,b,c,r):
    base = 2 ** (r-1)
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
        u,v = ops.divmod_sp(uv,base,r-1)
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
def cal(A,B,r):
    A_rev = A[::-1]
    B_rev = B[::-1]
    C_rev = [0] * (len(A) + len(B))
    base = 2 ** (r-1)
   
    # main procedure
    t1 = time.process_time()
    C_rev = _mul(A_rev,B_rev,C_rev,r)
    t2 = time.process_time()
    print('cpu time:',t2-t1)
    C = C_rev[::-1]

    print(f'CM res: {C} base {base}')
    return C

if __name__=='__main__':
    a = [[2, '-1'], [0, '-1'], [7, '-1']] # 1000 0111
    b = [[2, '-1'], [0, '-1'], [7, '-1']] # 1000 0111
    r = 4
    res = cal(a,b,r)
