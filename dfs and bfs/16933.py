import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline

n, m, k = map(int, input().split())
g = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, 0, True, 0))
    for i in range(k):
        visited[0][0][i] = 1
    while q:
        x, y, br, now, p = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][br]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if g[nx][ny] == 1:
                if br < k and visited[nx][ny][br+1] == 0:
                    if now:
                        visited[nx][ny][br+1] = visited[x][y][br] + 1 + p
                        q.append((nx, ny, br+1, not now, 0))
                    else:
                        q.append((x, y, br, not now, 1))
            else:
                if visited[nx][ny][br] == 0:
                    visited[nx][ny][br] = visited[x][y][br] + 1
                    q.append((nx, ny, br, not now, 0))
    return -1

print(bfs())
