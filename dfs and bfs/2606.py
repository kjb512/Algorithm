from collections import deque

n = int(input())

e = int(input())

g = [[] for _ in range(n)]

for i in range(e):
    n1, n2 = map(int, input().split())
    g[n1 - 1].append(n2 - 1)
    g[n2 - 1].append(n1 - 1)

d = [False] * n


def bfs(g, s, d):
    count = 0
    q = deque()
    q.append(s)
    d[s] = True

    while q:
        n = q.popleft()
        for i in g[n]:
            if not d[i]:
                count += 1
                q.append(i)
                d[i] = True


    return count

print(bfs(g,0,d))