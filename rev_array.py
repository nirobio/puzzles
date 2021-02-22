#!/bin/python3

import math
import os
import random
import re
import sys


def reverseArray(a):
    revArr = []
    x = 1
    for i in range(arr_count):
        revArr.append(arr[-x])
        x += 1
    return revArr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
