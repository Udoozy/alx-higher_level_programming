#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    Last_number = number % -10
else:
    Last_number = number % 10
if Last_number > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, Last_number))
elif Last_number < 6 and Last_number != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, Last_number))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
