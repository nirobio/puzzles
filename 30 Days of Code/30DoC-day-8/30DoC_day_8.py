# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import os
import random
import re
import sys

# first line of input signifies n
# accept input in format name (lowercase) + " " + 8-digit number
# key value pair = name+ "=" phoneNumber

# when only name entered, output phoneNumber in format above
# if name not in db, output = "Not Found"

n = int(input())
i = 0
phoneBook = dict()
while(i < n):
    name , number = input().split()
    phoneBook[name] = number
    i+=1
while True:
    try:
        nameQuery = input()
    except:
        break
    value = phoneBook.get(nameQuery, 0)
    if value != 0:
        print(nameQuery + "=" + phoneBook[nameQuery])
    else:
        print("Not found")
