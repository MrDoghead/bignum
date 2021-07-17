import sys
import opt
import argparse
from opt import add,multiply
from utils import convert, process
from utils import reporter


def check_input(args):
    n1 = args.num1
    op = args.op
    n2 = args.num2
    n = args.n
    r = args.r
    ub = args.ub
    max_range = 1 << (n-1)

    if op not in opt.__all__:
        print('Invalid operator!')
        sys.exit()
    if r <= ub:
        print("Invalid -r or -ub!")
        sys.exit()
    if abs(n1 * n2) >= max_range:
        print("Overflow!")
        sys.exit()
    print(f"to compute INT{n} {n1} {op} {n2} using INT {args.r} with unavailable bits {ub}")

def compute(A,B,args):
    op = args.op
    if op == '+':
        print('## No implement:',op)
        sys.exit()
        #rep = reporter.Reporter('add opts',args)
        #res = add.cal(A,B,args,rep)
    elif op == '-':
        print('## No implement:',op)
        sys.exit()
    elif op == 'x':
        rep = reporter.Reporter('mul opts',args)
        res,rep = multiply.cal(A,B,args,rep)
    elif op == '/':
        print('## No implement:',op)
        sys.exit()

    return res,rep


def main():
    parser = argparse.ArgumentParser(description='classic_multiplication')
    parser.add_argument("num1", help="the first decimal number", type=int)
    parser.add_argument("op", help="specify the operator", type=str)
    parser.add_argument("num2", help="the second decimal number", type=int)
    parser.add_argument("-n", help="the dtype INT n of num1 and num2", default=16, type=int)
    parser.add_argument("-r", help="the base is 2^r", default=4, choices=[2,4], type=int)
    parser.add_argument("-ub", help="the Unavailable Bits in INT r", default=0, type=int)
    args = parser.parse_args()

    # check valid args
    check_input(args)

    # pre-process the input
    A, B = process.pre_process(args)

    # compute the results
    C,reporter = compute(A,B,args)

    # post-process the res
    result = process.post_process(C,args)

    print('final result base 10:',result)
    reporter.report()

    # check answer
    if args.op == '+':
        print('correct answer is', args.num1 + args.num2)
    elif args.op == '-':
        print('correct answer is', args.num1 - args.num2)
    elif args.op == 'x':
        print('correct answer is', args.num1 * args.num2)
    elif args.op == '/':
        print('correct answer is', args.num1 / args.num2)


if __name__=='__main__':
    # examples:
    # python main.py 123 x 321 -n 16 -r 4
    # python main.py 12345 x 54321 -n 32 -r 4 -ub 0
    # python main.py 1234567 x 7654321 -n 64 -r 4 -ub 1
    main()
