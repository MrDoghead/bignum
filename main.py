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
    r = args.r
    ub = args.ub

    if op not in opt.__all__:
        print('Invalid operator!')
        sys.exit()
    elif r <= ub:
        print("Invalid r or ub!")
        sys.exit()
    else:
        print(f"to compute {n1} {op} {n2} using INT {args.r} with unavailable bits {ub}")

def compute(A,B,args):
    op = args.op
    if op == '+':
        rep = reporter.Reporter('add',args)
        res = add.cal(A,B,args,rep)
    elif op == '-':
        print('No service!')
        sys.exit()
    elif op == 'x':
        rep = reporter.Reporter('mul',args)
        res,rep = multiply.cal(A,B,args,rep)
    elif op == '/':
        print('No service!')
        sys.exit()

    return res,rep


def main():
    parser = argparse.ArgumentParser(description='classic_multiplication')
    parser.add_argument("num1", help="the first decimal number", type=int)
    parser.add_argument("op", help="specify the operator", type=str)
    parser.add_argument("num2", help="the second decimal number", type=int)
    parser.add_argument("-r", help="the base is 2^r", default=4, choices=[2,4,6,8], type=int)
    parser.add_argument("-ub", help="the Unavailable Bits in INT r", default=1, type=int)
    args = parser.parse_args()

    # check valid args
    check_input(args)

    # pre-process the input
    sign1,A,sign2,B = process.pre_process(args)

    # compute the results
    C,reporter = compute(A,B,args)

    # post-process the res
    result = process.post_process(C,sign1,sign2,args)

    print('final result base 10:',result)

    reporter.report()

    # check answer
    print('To check the answer:')
    if args.op == '+':
        print('correct answer is', args.num1 + args.num2)
    elif args.op == '-':
        print('correct answer is', args.num1 - args.num2)
    elif args.op == 'x':
        print('correct answer is', args.num1 * args.num2)
    elif args.op == '/':
        print('correct answer is', args.num1 / args.num2)


if __name__=='__main__':
    # we define INT r is base 2^r.
    # examples:
    # python main.py 1234567 x 7654321 -r 4
    # python main.py 135 x 135 -r 4 -ub 2
    # python main.py 12345678 x 87654321 -r 4 -ub 1
    # python main.py 12345678 x 87654321 -r 2
    main()
