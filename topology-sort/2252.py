import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())


degree = [0] * (n+1)
g = [[]for _ in range(n+1)]

q = deque()

for _ in range(m):
    a, b = map(int, input().strip().split())
    g[a].append(b)
    degree[b] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)


res = []
while q:
    v = q.popleft()
    res.append(v)
    for nv in g[v]:
        degree[nv] -= 1
        if degree[nv] == 0:
            q.append(nv)


print(*res)
