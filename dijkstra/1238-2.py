import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m, x = map(int, input().split())

e = [[]for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    e[a].append((b, t))

INF = 1e9


def dijkstra(start):
    d = [INF] * (n+1)
    d[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        dist, node = heappop(q)

        if d[node] < dist:
            continue

        for nv, nw in e[node]:
            cost = nw + dist
            if cost < d[nv]:
                d[nv] = cost
                heappush(q, (cost, nv))

    return d


ans = dijkstra(x)

for i in range(1, n+1):
    if ans[i] == INF or ans[i] == 0:
        continue

    ans[i] += dijkstra(i)[x]