#! /usr/bin/env python3

def get_input():
    number = int(input('Enter the number: '))
    return number

def fibonacci_math(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def main():
    input_num = get_input()
    fibonacci_number = fibonacci_math(input_num)
    print('The Fibonacci number for', input_num, 'is', fibonacci_number)

if __name__ == '__main__':
    main()
