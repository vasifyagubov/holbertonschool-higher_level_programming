#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10 if number >= 0 else number % 10 - 10
print("Last digit of {} is {} ".format(number, num), end="")

if num > 5:
    print("and is greater than 5")
elif num == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
