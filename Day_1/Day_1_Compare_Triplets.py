import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    i,x,y = 0,0,0
    while i < len(a):
        if a[i] > b[i]:
            x+=1
            i+=1;
        elif a[i] < b[i]:
            y+=1
            i+=1;
        else:
            x+=0
            y+=0
            i+=1;
    return x,y;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
