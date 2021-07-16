import sys
from bignum.utils import convert

# convert int to bin
# split bin into t pieces
# Note the unavailable bits `-ub` in INT `-r` is represented as 0
# due to the physical uncertainty
# e.g. int 123 INT -r 4 -ub 1
# -> binary: 0111 1011
# -> [['0', '0', '1', '0'], ['1', '1', '1', '0'], ['0', '1', '1', '0']]
def split_num(num,n,r,ub):
    sign,num_bin = convert.dec2bin(num,n)
    print(f'INT{n} {num} in binary: {num_bin}')
    num_list = []
    block = []
    r2 = r - ub
    l = len(num_bin)
    pad = num_bin[0]
    num_bin = pad * (r2 - (l % r2)) + num_bin
    for i in range(len(num_bin)):
        k = len(num_bin) - i - 1
        if i != 0 and i % r2 == 0:
            block = block[::-1] + [0] * ub
            num_list.append(block)
            block = []
        block.append(int(num_bin[k]))
    block = block[::-1] + [0] * ub
    num_list.append(block)
    n_block = len(num_list)

    num_list = num_list[::-1]
    print(f'split it to {n_block} INT{r2} \n {num_list}')
    return sign,num_list


# big num ->  INT r-1 num list
# 135 * -135 -> +,[2,-1],[0,-1],[7,-1]],-,[[2,-1],[0,-1],[7,-1]]
def pre_process(args):
    print('--- Preprocessing: ---')
    num1 = args.num1
    num2 = args.num2
    n = args.n
    r = args.r
    ub = args.ub
    sign1,A = split_num(num1,n,r,ub)
    sign2,B = split_num(num2,n,r,ub)

    return sign1, A, sign2, B

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
    A = 123
    #B = 12345678
    B = 87654321 
    sign, res = split_num(A,16,4,1)
    print(sign,res)

    #C = [0,4,7,3,1]
    #pos = post_process(C,4)
    #print(pos)
