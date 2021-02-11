#!/bin/python3

import os
import sys
import datetime

# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    if "PM" in s:
        s=s.replace("PM"," ")
        t= s.split(":")
        if t[0] != '12':
            t[0]=str(int(t[0])+12)
            s= (":").join(t)
        return s
    else:
        s = s.replace("AM"," ")
        t= s.split(":")
        if t[0] == '12':
            t[0]='00'
            s= (":").join(t)
        return s


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
