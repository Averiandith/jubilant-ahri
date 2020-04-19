# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr = sorted(arr)
    maximum = arr[-1]
    for item in reversed(arr):
        if item != maximum:
            print(item)
            break
