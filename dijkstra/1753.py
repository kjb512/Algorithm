import sys
from heapq import heappop, heappush

input = sys.stdin.readline

INF = 1e9
v, e = map(int, input().split())
start = int(input().strip())
g = [[]for _ in range(v+1)]
for _ in range(e):
    u, ve, w = map(int, input().split())
    g[u].append((ve,w))

d = [INF] * (v+1)

q = []

def dijkstra():
    d[start] = 0
    heappush(q, (0, start))

    while q:
        distance, nv = heappop(q)
        for vertex, weight in g[nv]:
            cost = distance + weight
            if cost < d[vertex]:
                d[vertex] = cost
                heappush(q, (cost, vertex))

dijkstra()

for i in d[1:]:
    if i != INF:
        print(i)
    else:
        print("INF")


