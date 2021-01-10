#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    num = int(input())

for i in range(1, 11):
    answer = num * i
    print(num, 'x', i, '=', answer, sep=' ')
