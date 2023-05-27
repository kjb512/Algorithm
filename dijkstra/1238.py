import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m, x = map(int, input().split())

INF = 1e9
g = [[]for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int, input().split())
    g[u].append((v,w))

def dijkstra(start):
    d = [INF] * (n + 1)
    q = []
    d[start] = 0
    heappush(q, (0, start))
    while q:
        dist, node = heappop(q)

        if d[node] < dist:
            continue

        for nv, nw in g[node]:
            cost = nw+dist
            if cost < d[nv]:
                d[nv] = cost
                heappush(q, (cost, nv))

    return d

ans = dijkstra(x)
for i in range(1, n+1):
    if ans[i] == INF or ans[i] == 0:
        continue

    ans[i] += dijkstra(i)[x]

f = 0
for a in ans:
    if a == 0 or a == INF:
        continue
    if f < a:
        f = a
print(f)