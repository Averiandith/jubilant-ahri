# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem

def fibonacci(n):
    prev, curr = 0, 1
    while True:
        if n == 0:
            return prev
        if n == 1:
            return curr
        prev, curr = curr, prev + curr
        n -= 1
