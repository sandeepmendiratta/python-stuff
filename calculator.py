#!/usr/bin/env python3
""""
Calculator. Provides two digits and operation

"""


def calu(a,b,op):
    if op not in '+-/*':
        return 'Please only type one of these characters: "+, -, *, /"!'

    if op == '+':
        return (str(a) + ' ' + op + ' '+ str(b) + ' ' + '==' +  ' ' + str(a + b))
    if op == '-':
        return (str(a) + ' ' + op + ' '+ str(b) + ' ' + '==' +  ' ' + str(a - b))
    if op == '/':
        return (str(a) + ' ' + op + ' '+ str(b) + ' ' + '==' +  ' ' + str(a / b))
    if op == '*':
        return (str(a) + ' ' + op + ' '+ str(b) + ' ' + '==' +  ' ' + str(a * b))


def main():
    a = int(input("enter first number :"))
    b = int(input("enter 2nd number :"))
    op = (input(" Enter operation +/1* :"))

    print(calu(a,b,op))



if __name__ == '__main__':
    main()
