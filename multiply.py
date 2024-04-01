#! /usr/bin/env python3 

def get_input():
    size = int(input("Enter the size of your table: " ))
    return size


def print_table(n):

    cell_width = len(str((n * n))) + 1

    for i in range(1,n+1):
        for j in range(1, n+1):
            print("{:>{cell_width}}".format(i * j, cell_width = cell_width), end='')
        print()
    
def main():
    input_num = get_input()
    
    print_table(input_num)
    
if __name__ == '__main__':
    main()