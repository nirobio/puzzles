#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    lrDiagonal = []
    rlDiagonal = []
    lr_a = 0
    rl_a = n - 1
    for i in arr:
        lrDiagonal.append(i[lr_a])
        rlDiagonal.append(i[rl_a])
        lr_a += 1
        rl_a -= 1

    lr_total = sum(lrDiagonal)
    rl_total = sum(rlDiagonal)

    if rl_total >= lr_total:
        diff = rl_total - lr_total
    else:
        diff = lr_total - rl_total

    return diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
