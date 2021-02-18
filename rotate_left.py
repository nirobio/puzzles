#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# https://www.hackerrank.com/challenges/array-left-rotation/problem

def rotateLeft(d, arr):
    d = d % len(arr)
    arr = arr[d:] + arr[:d]
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
