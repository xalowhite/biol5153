#! /usr/bin/env python3

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='This script returns the Fibonacci numebr at \
        at a specified location in the Fibonacci sequence')
    
    parser.add_argument('num', help='The Fibonacci number you wish to calculate', type=int)
    parser.add_argument('-v', '--verbose', help='Print verbose output or not', action='store_true')
    
    args = parser.parse_args()
    return args


def fibonacci_math(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def main():
    fibonacci_number = fibonacci_math(args.num)
    if args.verbose:
        print('The Fibonacci number for', args.num, 'is', fibonacci_number)
    else:
        print(fibonacci_number)
        
args = get_args()


if __name__ == '__main__':
    main()

