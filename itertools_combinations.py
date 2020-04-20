# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations


if __name__ == "__main__":
    string, size = input().split(" ")
    string, size = sorted(string), int(size)

    for i in range(1, size + 1):
        for combination in combinations(string, i):
            print("".join(combination))
