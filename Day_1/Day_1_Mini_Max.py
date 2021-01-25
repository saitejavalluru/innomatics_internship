import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    maxi = sum(arr,0) - max(arr)
    mini = sum(arr,0) - min(arr)
    print(maxi,mini);

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
