import math
import os
import random
import re
import sys

# Complete the stockmax function below
def stockmax(prices):
    max = 0
    profit = 0
    for i in range(len(prices)-1, -1, -1):
    	if max < prices[i]:
    		max = prices[i]
    	profit += max - prices[i]
    return profit


if __name__ == "__main__":
    prices = [1, 2, 100]
    result = stockmax(prices)
    print(result)

