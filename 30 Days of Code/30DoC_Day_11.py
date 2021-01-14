#!/bin/python3

import math
import os
import random
import re
import sys

#    arr[0][0], arr[0][1], arr[0][2]
#    arr[1][1]
#    arr[2][0]. arr[2][1], arr[2][2]
if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


hgSum = []

for row in range(0, 4):
    for column in range(0, 4):
        add = sum(arr[row][column:column + 3]) + arr[row +
                                                     1][column + 1] + sum(arr[row + 2][column:column + 3])
        hgSum.append(add)

print(max(hgSum))
