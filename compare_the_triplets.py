import math
import os
import random
import re
import sys



def compareTriplets(a,b):
    alice_score = 0;
    bob_score = 0;

    for x,y in zip(a,b):

        if x > y:
            alice_score +=1;

        elif x < y:
            bob_score +=1;

    return [alice_score, bob_score]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a,b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
