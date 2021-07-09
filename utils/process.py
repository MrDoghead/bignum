import sys
from bignum.utils import convert

# change int to bin
# split bin into t pieces
# Note the last bit in INT r is represented as -1 (just a mark)
# due to the physical uncertainty
# e.g. int 135 INT 4 ub 1
# -> [1,0,0,0,0,1,1,1] 
# -> [['1', '0', '-1'], ['0', '0', '0', '-1'], ['1', '1', '1', '-1']]
def split_num(num,r,ub):
    sign, num_bin = convert.dec2bin(num)
    print(f'{num} binary: {num_bin}')
    num_list = []
    n = []
    r2 = r - ub
    for i in range(len(num_bin)):
        k = len(num_bin) - i - 1
        if i != 0 and i % r2 == 0:
            n = n[::-1] + ['-1'] * ub
            num_list.append(n)
            n = []
        n.append(num_bin[k])
    n = n[::-1] + ['-1'] * ub
    num_list.append(n)
    n_block = len(num_list)

    num_list = num_list[::-1]
    print(f'split it to {n_block} INT {r2} \n {num_list}')
    return sign, num_list

def _trans(num_list,ub):
    res = []
    for each in num_list:
        bi = ''.join(each[:-ub])
        res.append([int(bi,2), each[-ub:]])
    return res

# big num ->  INT r-1 num list
# 135 * -135 -> +,[2,-1],[0,-1],[7,-1]],-,[[2,-1],[0,-1],[7,-1]]
def pre_process(args):
    num1 = args.num1
    num2 = args.num2
    r = args.r
    ub = args.ub
    sign1, A = split_num(num1,r,ub)
    sign2, B = split_num(num2,r,ub)

    # bin to dec
    A2 = _trans(A,ub)
    B2 = _trans(B,ub)
        
    print(f'after preprocessing: {A2} x {B2}')
    return sign1, A2, sign2, B2

def post_process(nums,sign1,sign2,args):
    n = len(nums)
    res = 0
    r = args.r
    ub = args.ub
    base = 2 ** (r - ub)
    for i in range(n):
       res += nums[i] * (base ** (n-i-1))
    
    if sign1 == sign2:
        res = str(res)
    else:
        res = '-' + str(res)

    return res

if __name__=='__main__':
    A = 135
    #B = 12345678
    B = 87654321 
    sign,res = split_num(A,4,2)
    print(sign,res)

    #C = [0,4,7,3,1]
    #pos = post_process(C,4)
    #print(pos)
