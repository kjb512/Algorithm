import sys
from collections import deque

input = sys.stdin.readline

n,m,k= map(int,input().split())
g = [list(map(int, input().strip())) for _ in range(n)]
v = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque()
    q.append((0,0,0))
    for i in range(k):
        v[0][0][i] = 1

    while q:
        x, y, f = q.popleft()

        if x == n-1 and y == m-1:
            return v[x][y][f]

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if not(0 <= nx < n and 0 <= ny < m):
                continue

            if g[nx][ny] == 1 and f < k and v[nx][ny][f+1] ==0:
                q.append((nx,ny,f+1))
                v[nx][ny][f+1] = v[x][y][f] + 1
            elif g[nx][ny] == 0 and v[nx][ny][f] == 0:
                q.append((nx,ny,f))
                v[nx][ny][f] = v[x][y][f] + 1

    return -1

print(bfs())
