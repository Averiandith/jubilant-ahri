# https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s, d, m):
    chunks = [s[i:i + m]
              for i in range(len(s) - m + 1)]
    return sum(1 if sum(chunk) == d else 0
               for chunk in chunks)
