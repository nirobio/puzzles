#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/mini-max-sum/problem


def miniMaxSum(arr):
    sortedArr = sorted(arr)
    smallest = sum(sortedArr) - sortedArr[-1]
    largest = sum(sortedArr) - sortedArr[0]
    print(str(smallest) + " " + str(largest))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
