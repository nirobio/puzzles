# given set S = {1,2,3, ...,N}, find two integers, A & B (where A < B).
# from set S, such that the value of A&B is the max. possible and also
# less than a given integer, K. In this case, & represents the bitwise
# AND operator.

# input = N and K, respectively.

# Operator	Example	 Meaning
#    &	     a & b	 Bitwise AND
#    |	     a | b	 Bitwise OR
#    ^	     a ^ b	 Bitwise XOR (exclusive OR)
#    ~      ~a	     Bitwise NOT
#    <<	     a << n	 Bitwise left shift
#    >>	     a >> n	 Bitwise right shift

#!/bin/python3

import math
import os
import random
import re
import sys


t = int(input())


for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    maxDiff = 0


    for i in range(1, n):
        for j in range(i+1, n+1):
            result = i & j
            if k > result > maxDiff:
                maxDiff = result


    print(maxDiff)
