# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement


if __name__ == "__main__":
    string, size = input().split(" ")
    string, size = sorted(string), int(size)

    for combination in combinations_with_replacement(string, size):
        print("".join(combination))
