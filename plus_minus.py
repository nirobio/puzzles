#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/rest/contests/master/challenges/plus-minus/

positive = []
negative = []
zero = []


def plusMinus(arr):
    for i in arr:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            zero.append(i)

    pctPositive = len(positive) / n
    pctNegative = len(negative) / n
    pctZero = len(zero) / n

    print("%.6f" % pctPositive)
    print("%.6f" % pctNegative)
    print("%.6f" % pctZero)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
