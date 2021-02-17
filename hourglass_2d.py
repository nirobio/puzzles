#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/2d-array/problem
def hourglassSum(arr):
    hgSum = []

    for row in range(0, 4):
        for column in range(0, 4):
            add = sum(arr[row][column:column + 3]) + arr[row +
                                                         1][column + 1] + sum(arr[row + 2][column:column + 3])
            hgSum.append(add)
    maximum = max(hgSum)
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
