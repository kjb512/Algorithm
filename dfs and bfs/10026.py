import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline
n = int(input())
g = [list(input().strip()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

def bfs(a,b):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < n and 0<= ny < n):
                continue
            if not visited[nx][ny] and g[nx][ny] == g[x][y]:
                visited[nx][ny] = True
                q.append((nx, ny))

def bfs2(a,b):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < n and 0<= ny < n):
                continue
            if not visited[nx][ny] and (g[nx][ny] == g[x][y] or (g[nx][ny] != 'B' and g[x][y] != 'B')):
                visited[nx][ny] = True
                q.append((nx, ny))


cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1

visited = [[False] * n for _ in range(n)]

cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs2(i, j)
            cnt2 += 1
print(cnt, cnt2)