import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))


st, en = map(int, input().split())
INF = 1e9
d = [INF] * (n+1)
d[st] = 0
q = []
heapq.heappush(q, (0, st))
while q:
    dist, v = heapq.heappop(q)
    if d[v] < dist:
        continue

    for nv, nc in g[v]:
        cost = dist + nc
        if cost < d[nv]:
            d[nv] = cost
            heapq.heappush(q, (cost, nv))

print(d[en])

