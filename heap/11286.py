import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
h = []

for i in range(n):
    x = int(input())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heappop(h)[1])
    else:
        heappush(h, (abs(x), x))