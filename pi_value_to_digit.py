#!/usr/bin/env python3


""""Find PI to the Nth Digit -
Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go."""

import math


def getValueOfPi(k):
    return '%.*f' % (k, math.pi)


def main():
    """
    Console Function to create the interactive Shell.
    Runs only when __name__ == __main__ that is when the script is being called directly
    No return value and Parameters
    """
    print("Welcome to Pi Calculator. In the shell below Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit")

    while True:
        try:
            entry = int(input("How many spaces? "))
            if entry > 50:
                print("Number to large")
            # elif str(entry) == "quit":
            #     break
            else:
                print(getValueOfPi(int(entry)))
        except:
            print("You did not enter an integer")




if __name__ == '__main__':
    main()