import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline

n, m = map(int, input().strip().split())
g = [list(map(int, input().strip()))for _ in range(n)]
v = [[[0] * 2 for _ in range(m)]for _ in range(n)]

q = deque()
q.append((0, 0, 0))
v[0][0][0] = 1
v[0][0][1] = 1

while q:
    x, y, b = q.popleft()

    if x == n-1 and y == m-1:
        print(v[x][y][b])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if g[nx][ny] == 1:
                if b == 0 and v[nx][ny][1] == 0:
                    v[nx][ny][1] = v[x][y][0] + 1
                    q.append((nx, ny, 1))
            else:
                if v[nx][ny][b] == 0:
                    v[nx][ny][b] = v[x][y][b] + 1
                    q.append((nx, ny, b))
