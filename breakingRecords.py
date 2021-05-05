#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

n = int(input())
scores = list(map(int, input().rstrip().split()))

best = scores[0]
worst = scores[0]
x = 0
y = 0

for i in scores:
    if i > best:
        best = i
        x += 1

    elif i < worst:
        worst = i
        y += 1
print(x, y)
