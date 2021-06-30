import sys

def check_overflow(num,n,r):
    upper = 0
    for i in range(n):
        upper += r ** i

    return True if num > upper else False

def trans_map(cint):
    if cint < 0:
        print("invalid")
        return
    elif cint < 10:
        return cint

    elif cint >= 10:
        return chr(cint - 10 + 65)

# int m to int n
def transfer(m, n, origin):
    num = anyToTen(m, origin)
    target = tenToAny(n, num)
    print(target)

# int m to int 10
def anyToTen(m, origin):
    return int(str(origin), base=m)

# int 10 to int n
def tenToAny(n, origin):
    list = []
    while True:
        s = origin // n
        tmp = origin % n
        list.append(trans_map(tmp))
        if s == 0:
            break
        origin = s
    list.reverse()
    list = [str(each) for each in list]
    print(''.join(list))

def conv_int(num,n,r):
    if check_overflow(num,n,r):
        print('overflow happened')
        sys.exit()
    num_list = [0] * n

def dec2bin(n):
    return bin(n).split('b')[-1]


if __name__ == '__main__':
    pass
