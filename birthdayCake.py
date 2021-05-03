#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/birthday-cake-candles/problem


def birthdayCakeCandles(candles):
    lenLargest = 0
    largest = max(candles)
    for i in range(len(candles)):
        if (candles[i] == largest):
            lenLargest += 1
    return lenLargest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
