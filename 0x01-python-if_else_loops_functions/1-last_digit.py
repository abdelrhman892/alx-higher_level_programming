#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastDigit = int(repr(number)[-1])
if number < 0:
    lastDigit = lastDigit * -1
if (lastDigit > 5) and (number > 0):
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif (lastDigit < 6) and (lastDigit != 0):
    print(f"Last digit of {number} is {lastDigit} and is "
          f"less than 6 and not 0")
elif lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
