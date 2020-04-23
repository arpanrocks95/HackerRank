#!/bin/python3

import math
import random
import re


# Complete the reverseArray function below.
def reverseArray(a):
    b = []
    for i in a[::-1]:
        b.append(i)
    return b
if __name__ == '__main__':
    

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(res)


