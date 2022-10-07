from collections import deque

n = int(input())

a, b = map(int, input().split())

k = int(input())

g = [[] for _ in range(n)]

for _ in range(k):
    g1, g2 = map(int, input().split())
    g[g1-1].append(g2-1)
    g[g2-1].append(g1-1)

d = [0] * n

def bfs(g, a, b, d):
    q = deque()
    q.append(a)
    d[a] = 1

    while q:
        v = q.popleft()
        for i in g[v]:
            if d[i] == 0:
                d[i] += d[v] + 1
                if i == b:
                    return d[i]
                q.append(i)

bfs(g,a-1,b-1,d)

if d[b-1] == 0:
    print(-1)
else:
    print(d[b-1]-1)
