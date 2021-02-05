#!/bin/python3

import math
import os
import random
import re
import sys

GmailNames = []

n = int(input())

for i in range(n):
    firstNameEmailID = str(input()).split(" ")
    firstName = firstNameEmailID[0]
    emailID = firstNameEmailID[1]
    i += 1

    if re.search(".+@gmail\.com$", emailID):
        GmailNames.append(firstName)

GmailNames.sort()

for name in GmailNames:
    print(name)
