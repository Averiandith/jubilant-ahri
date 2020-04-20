# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    counterparts = [[item for item in ar[i + 1:]]
                    for i in range(n)]
    return sum(1 if (first + second) % k == 0 else 0
               for i, first in enumerate(ar)
               for second in counterparts[i])
