#!/bin/python3
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swapCount = 0
# bubble sort
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            swapCount += 1

print("Array is sorted in " + '%d' % swapCount + " swaps.")
print("First Element: " + '%s' % a[0])
print("Last Element: " + '%s' % a[-1])
