#!/bin/python3

import math
import os
import random
import re
import sys


num = int(input("Enter a number: "))
if (num % 2) != 0:
    print("Weird")

elif ((num % 2) == 0) and (1 < num < 6):
    print("Not Weird")

elif ((num % 2) == 0) and (5 < num < 21):
    print("Weird")
elif ((num % 2) == 0) and (num > 20):
    print("Not Weird")


if __name__ == '__main__':
    num = int(input())
