#! /usr/bin/env python3

import say_hello

def main():
    name = input('Enter a name: ')
    say_hello.greeting(name)

    fav  = input("What's your favorite?")
    say_hello.favorite(fav)
    
    
    
if __name__ == '__main__':
    main()