import sys

def complement(num):
    # 2's complement
    tmp = num[0]
    for i in range(1,len(num)):
        if num[i] == '0':
            tmp += '1'
        elif num[i] == '1':
            tmp += '0'
    res = bin(int(tmp,2) + 1)
    res = res.split('0b')[-1]
    assert len(res) == len(num)
    #print(f'convert negative number {num} to its complement {res}')

    return res

def list2bin(nums,r):
    res = ''
    for num in nums:
        res += dec2bin(num,r)
    #print('bins:',res)
    return res
    
def dec2bin(num,n):
    bits = bin(num).split('0b')[-1]
    if len(bits) > n:
        print(f'Cannot convert to binary with {n} bits!')
        sys.exit()
    # padding to INT n
    # the first bit represents the +/- sign
    if num >= 0:
        res = '0' * (n-len(bits)) + bits
    else:
        bits = '1' + '0' * (n-len(bits)-1) + bits
        res = complement(bits)

    return res

if __name__ == '__main__':
    n1 = dec2bin(12345,16)
    n2 = dec2bin(-12345,16)
    print(n1,n2)


