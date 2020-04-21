# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product


if __name__ == '__main__':
    a = [int(i) for i in input().split(" ")]
    b = [int(i) for i in input().split(" ")]

    for pair in product(a, b):
        print(pair, end=" ")
