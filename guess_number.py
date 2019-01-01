import random

a = random.randint(1, 10)
print('Number to guess, {}'.format(a))
b = 0

while b != a:
    b = int(input("Please input a number from 1 to 10 to guess :"))
    if b > a:
        print("the number you guessed is too high")
    else:
        print("the number you guessed is too low")
    if a == b:
        print("You guessed it right, done!")