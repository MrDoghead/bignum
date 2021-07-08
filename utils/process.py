import sys
from bignum.utils import convert

# change int to bin
# split bin into t pieces
# Note the last bit in INT r is represented as -1 (just a mark)
# due to the physical uncertainty
# e.g. int 135
# -> [1,0,0,0,0,1,1,1] 
# -> [['1', '0', '-1'], ['0', '0', '0', '-1'], ['1', '1', '1', '-1']]
def split_num(num,r):
    sign, num_bin = convert.dec2bin(num)
    print(f'{num} binary: {num_bin}')
    num_list = []
    n = []
    r2 = r - 1
    for i in range(len(num_bin)):
        k = len(num_bin) - i - 1
        if i != 0 and i % r2 == 0:
            n = n[::-1] + ['-1']
            num_list.append(n)
            n = []
        n.append(num_bin[k])
    n = n[::-1] + ['-1']
    num_list.append(n)
    n_block = len(num_list)

    num_list = num_list[::-1]
    print(f'split it to {n_block} INT {r2} \n {num_list}')
    #num_list2 = [''.join(each) for each in num_list]
    #res = [int(each,2) for each in num_list2]
    return sign, num_list

# big num ->  INT r num list
# 135 -> [8,7]_4
def pre_process(args):
    num1 = args.num1
    num2 = args.num2
    r = args.r
    sign1, A = split_num(num1,r)
    sign2, B = split_num(num2,r)

    # bin to dec
    A2 = []
    B2 = []
    for each in A:
        binA = ''.join(each[:-1])
        A2.append([int(binA,2),each[-1]])
    for each in B:
        binB = ''.join(each[:-1])
        B2.append([int(binB,2),each[-1]])
        
    print(f'after preprocessing: {A2} x {B2}')
    return sign1, A2, sign2, B2

def post_process(nums,r,sign1,sign2):
    n = len(nums)
    res = 0
    base = 2 ** (r-1)
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
    print(split_num(A,4))

    #C = [0,4,7,3,1]
    #pos = post_process(C,4)
    #print(pos)
