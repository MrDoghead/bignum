# define defferent operators

def add(a,b):
    return a + b

def mul(a,b,r,ub):
    ar = a[::-1]
    br = b[::-1]
    cr = [0] * (len(a)+len(b))
    for i in range(len(br)):
        carry = 0
        for j in range(len(ar)):
            uv = cr[i+j] + br[i] * ar[j] + carry
            u,v = divmod_sp(uv,2,1)
            cr[i+j] = v
            carry = u
        cr[i+j+1] = u
    
    if ub == 0:
        c = cr[::-1]
    else:
        c = cr[::-1][:-2*ub]
    #print('C:',c)
    s = [str(i) for i in c]
    return int(''.join(s),2)

# x / y = quotient + reminder
def divmod_sp(x,y,r):
    assert y == 2 ** r
    BASE = y - 1
    reminder = x & BASE
    quotient = x >> r

    return quotient,reminder

if __name__ == '__main__':
    #A = [1, 0, 0, 0]
    #B = [1, 0, 0, 0]
    #res = mul(A,B,4,1)
    res = divmod_sp(16,8,3)
    print(res)
