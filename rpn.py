#!/usr/bin/python

import operator
import readline
import sys
from termcolor import colored, cprint


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
   # '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result) 
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

print("Added Unmarked Code")
print("I wish I knew more python")
def main():
    while True:
        result = calculate(input("rpn calc> "))
        resultKeyword = colored("Return: ", "blue")
        
        if result < 0:
            result = colored(result, 'red')
        else: 
            result = colored(result, 'yellow') 
        
        print(resultKeyword,result)

if __name__ == '__main__':
    main()
