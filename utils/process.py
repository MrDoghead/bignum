import sys
from bignum.utils import convert

# split nums into t pieces
# decimal num -> binary num list -> decimal num list
# 135 -> [1,0,0,0,0,1,1,1] -> [8,7]
def split_num(num,r):
    num_bin = convert.dec2bin(num)
    print(f'{num} binary: {num_bin}')
    num_list = []
    n = []
    for i in range(len(num_bin)):
        k = len(num_bin) - i - 1
        if i != 0 and i % r == 0:
            n = n[::-1]
            num_list.append(n)
            n = []
        n.append(num_bin[k])
    n = n[::-1]
    num_list.append(n)
    n_block = len(num_list)

    num_list = num_list[::-1]
    print(f'split to {n_block} INT {r} \n {num_list}')
    num_list2 = [''.join(each) for each in num_list]
    res = [int(each,2) for each in num_list2]
    return res

# big num ->  INT r num list
# 135 -> [8,7]_4
def pre_process(args):
    num1 = args.num1
    num2 = args.num2
    r = args.r
    base = 2 ** r
    A = split_num(num1,r)
    B = split_num(num2,r)

    print(f'after pre_process: {A} * {B} base {base}')
    return A,B

def post_process(nums,r):
    n = len(nums)
    res = 0
    base = 2 ** r
    for i in range(n):
       res += nums[i] * (base ** (n-i-1))

    print(f'after post_process: {res}')
    return res

if __name__=='__main__':
    A = 135
    #B = 12345678
    B = 87654321 
    print(split_num(B,4))

    #C = [0,4,7,3,1]
    #pos = post_process(C,4)
    #print(pos)
