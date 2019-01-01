#!/usr/bin/env python3
""""Find e to the Nth Digit
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go"""


from math import e


def e_with_precision(n):
    """Return euler's number to the n-th decimal place
    :param n: number of decimal places to return
    :type n: int
    :return: euler's number with n decimal places
    :rtype: str
    """
    return '%.*f' % (n, e)

def main():
    correct_input = True
    while True:
        # ask until you get correct input
        print('Precision must be between 1 and 51')
        precision = int(input('Number of decimal places: '))
        if 51 >= precision > 0:
            print(e_with_precision(precision))

        else:
            correct_input = False
            print(" Number is too high quiting ")

            break



if __name__ == '__main__':
   main()