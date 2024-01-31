import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(input().strip()) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)]for _ in range(n)]
q = deque()
q.append((0,0,0))
visited[0][0][0] = 1
visited[0][0][1] = 1

while q:
    x, y, br = q.popleft()
    if x == n-1 and y == m-1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if g[nx][ny] == '0' and visited[nx][ny][br] == 0:
            visited[nx][ny][br] = visited[x][y][br] + 1
            q.append((nx, ny, br))
        elif g[nx][ny] == '1' and br == 0 and visited[nx][ny][br+1] == 0:
            visited[nx][ny][br+1] = visited[x][y][br] + 1
            q.append((nx, ny, br+1))

res = max(visited[n-1][m-1])
if res != 0:
    print(res)
else:
    print(-1)