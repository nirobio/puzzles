#!/bin/python3
# https://www.hackerrank.com/challenges/python-sort-sort/
import math
import os
import random
import re
import sys

# n = no. of rows
# m = no. of columns (attributes)
# k = sort by K'th attribute. k is zero-indexed

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())

    arr.sort(key=lambda x: x[k])

    for line in arr:
        print(*line, sep=' ')
