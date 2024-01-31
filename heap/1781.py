import sys
import heapq

input = sys.stdin.readline

n = int(input())

queue = []
res = 0
dl = [[]for _ in range(n+1)]
for _ in range(n):
    d, c = map(int, input().split())
    dl[d].append(c)

for t in range(n, 0, -1):
    for cup in dl[t]:
        heapq.heappush(queue, -cup)

    if not queue:
        continue

    res -= heapq.heappop(queue)


print(res)
