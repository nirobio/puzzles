#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/bon-appetit/problem


def bonAppetit(bill, k, b):
    total = sum(bill)
    notEaten = bill[k]
    AnnaShare = (total - notEaten) / 2
    if b == AnnaShare:
        print("Bon Appetit")
    else:
        outstanding = int(b - AnnaShare)
        print(outstanding)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
