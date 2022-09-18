# 피드백: 양방향일 경우 둘다 추가
from collections import deque

v, e, f = map(int, input().split())

g = [[] for _ in range(v + 1)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    g[v2].append(v1)

for i in range(len(g)):
    g[i].sort()

d = [False] * (v + 1)

def dfs(g, v, d):
    d[v] = True
    print(str(v), end=" ")
    for i in g[v]:
        if not d[i]:
            dfs(g, i, d)

def bfs(g, v, d):
    q = deque()
    q.append(v)
    print(str(v), end=" ")
    d[v] = True

    while q:
        x = q.popleft()
        for i in g[x]:
            if not d[i]:
                d[i] = True
                q.append(i)
                print(str(i), end=" ")

dfs(g, f, d)

d = [False] * (v + 1)
print()

bfs(g, f, d)