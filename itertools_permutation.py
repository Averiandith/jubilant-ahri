# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations


if __name__ == "__main__":
    string, size = input().split(" ")
    size = int(size)

    for permutation in sorted(permutations(string, size)):
        print("".join(permutation))
