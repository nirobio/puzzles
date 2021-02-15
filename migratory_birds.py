#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    arr.sort()
    freq = Counter(arr)
    maximum = (max(freq, key=freq.get))
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
