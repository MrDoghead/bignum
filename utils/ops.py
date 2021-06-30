# x / y = quotient + reminder
def divmod_sp(x,y,r):
    BASE = y - 1
    reminder = x & BASE
    quotient = x >> r

    return quotient,reminder

if __name__ == '__main__':
    res = divmod_sp(135,16,4)
    print(res)
