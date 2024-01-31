import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

hx = [1, 1, 2, 2, -1, -1, -2, -2]
hy = [2, -2, 1, -1, 2, -2, 1, -1]

k = int(input().strip())
w, h = map(int, input().strip().split())

g = [list(map(int, input().split())) for _ in range(h)]
v = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]

q = deque()

q.append((0, 0, 0))

def bfs():
    while q:
        x, y, cnt = q.popleft()

        if x == h-1 and y == w-1:
            return v[x][y][cnt]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if g[nx][ny] == 0 and v[nx][ny][cnt] == 0:
                    v[nx][ny][cnt] = v[x][y][cnt] + 1
                    q.append((nx, ny, cnt))

        for i in range(8):
            nx = x + hx[i]
            ny = y + hy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if g[nx][ny] == 0 and cnt < k and v[nx][ny][cnt+1] == 0:
                    v[nx][ny][cnt+1] = v[x][y][cnt] + 1
                    q.append((nx, ny, cnt+1))

    return -1


print(bfs())