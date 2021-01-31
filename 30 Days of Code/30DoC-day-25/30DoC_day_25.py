from math import sqrt
from sys import stdin

def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())
for x in stdin:
    y = int(x)
    if (y >= 2 and isPrime(y)):
        print("Prime")
    else:
        print("Not prime")
