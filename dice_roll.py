import random
import pprint

print("Starting Dice roll, Please roll the dice")

x = True
while x:
    a = (input("Would you like to roll the dice Y or N :"))
    if a is "Y":
        print(random.randint(1,6))
    else:
        x = False
        print("Game done !")





