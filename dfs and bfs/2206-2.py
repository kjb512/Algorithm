import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

g = [list(map(int, input().strip())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1, 1, 0, 0]
v = [[[0]*2 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    v[0][0][0] = 1
    v[0][0][1] = 1

    while q:
        x, y, f = q.popleft()

        if x == n-1 and y == m-1:
            return v[x][y][f]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if not (0<= nx < n and 0<=ny<m):
                continue

            if g[nx][ny] == 1:
                if f == 0 and v[nx][ny][1] == 0:
                    q.append((nx,ny,1))
                    v[nx][ny][1] = v[x][y][f] +1
            else:
                if v[nx][ny][f] == 0:
                    q.append((nx,ny,f))
                    v[nx][ny][f] = v[x][y][f] +1
    return -1

print(bfs())
