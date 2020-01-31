#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'predictAnswer' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stockData
#  2. INTEGER_ARRAY queries
#

def predictAnswer(stockData, queries):
    # Write your code here
    check = []
    neg = 1
    res = []

    for day in queries:
        left = day -1
        right = day +1
        if (stockData[day-2] in stockData) & (stockData[day-2] < stockData[day-1]):
            check.append(day-2)
        else:
            neg = neg -1
        if (stockData[day] in stockData) & (stockData[day] < stockData[day-1]):
            check.append(day)
        else:
            neg = neg -1
        
        if neg > -1:
            res.append(testStock(check, stockData))
        else: res.append('-1') 
    
    return res

def testStock(checkD, stockData):
    if (len(checkD) > 1) & (stockData[checkD[0]] > stockData[checkD[1]]):
        return (checkD[1] +1)
    else:
        return checkD[0]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stockData_count = int(input().strip())

    stockData = []

    for _ in range(stockData_count):
        stockData_item = int(input().strip())
        stockData.append(stockData_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = predictAnswer(stockData, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
