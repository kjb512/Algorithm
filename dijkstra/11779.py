import sys
from heapq import heappop, heappush

input = sys.stdin.readline

INF = 1e9
n = int(input().strip())
m = int(input().strip())
g = [[]for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v,w))

start, end = map(int, input().split())

d = [INF] * (n+1)
prev = [0] * (n+1)

def dijkstra():
    q = []
    heappush(q, (0, start))
    d[start] = 0
    while q:
        dist, node = heappop(q)
        if d[node] < dist:
            continue
        for nv, nw in g[node]:
            cost = nw + dist

            if cost < d[nv]:

                prev[nv] = node
                d[nv] = cost
                heappush(q,(cost, nv))
dijkstra()

print(d[end])

ans = [end]
i = end
while i != start:
    i = prev[i]
    ans.append(i)

ans.reverse()
print(len(ans))
print(' '.join(map(str, ans)))
