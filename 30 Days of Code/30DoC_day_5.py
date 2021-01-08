# Strings and loop
# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import os
import random
import re
import sys


s = int(input())

for i in range(0, s):
    strInput = input()
    print(strInput[0::2] + " " + strInput[1::2])
