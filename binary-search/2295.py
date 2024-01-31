import sys
from itertools import combinations
import bisect

input = sys.stdin.readline

n = int(input())

u = [int(input()) for _ in range(n)]

s = []

for i in range(n):
    for j in range(i, n):
        s.append(u[i] + u[j])

u.sort()
s.sort()
ls = len(s)
flag = False

for i in range(n - 1, -1, -1):
    for j in range(i, -1, -1):
        a = u[i] - u[j]
        idx = bisect.bisect_left(s, a)
        if idx != ls and s[idx] == a:
            print(u[i])
            flag = True
            break
    if flag:
        break