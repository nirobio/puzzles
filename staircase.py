#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/staircase/

space = " "
stair = "#"


def staircase(n):
    j = 1
    l = 1
    for i in range(n):
        print(((n - j) * space) + (l * stair))
        j += 1
        l += 1


if __name__ == '__main__':
    n = int(input())

    staircase(n)
