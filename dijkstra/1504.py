import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())

g = [[]for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

v1, v2 = map(int, input().split())

INF = 1e9

def dijkstra(start):

    d = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    d[start] = 0
    while q:
        cost, v = heapq.heappop(q)

        if d[v] < cost:
            continue

        for nv, nc in g[v]:
            c = cost + nc
            if d[nv] > c:
                d[nv] = c
                heapq.heappush(q, (c, nv))

    return d

d1 = dijkstra(v1)
d2 = dijkstra(v2)

c1 = d1[1] + d1[v2] + d2[n]
c2 = d2[1] + d2[v1] + d1[n]

res = min(c1, c2)
if res < INF:
    print(res)
else:
    print(-1)