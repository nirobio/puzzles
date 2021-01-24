#!/bin/python3

import sys

# print parsed integer value of S
# or print("Bad String")
# Note: You must use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a  score.

S = input().strip()

try:
    intS = int(S)
    print(intS)

except Exception:
    print("Bad String")
