import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    l = map(int, input().split())

    q = []
    for cost in l:
        heapq.heappush(q, cost)

    res = 0
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        c = a + b
        res += c
        heapq.heappush(q, c)

    print(res)
