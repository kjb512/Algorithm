from collections import deque

n, m = map(int, input().split())

g = [list(map(int, input())) for _ in range(n)]

v = [[[0]*2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    v[0][0][0] = v[0][0][1] = 1

    while q:
        x, y, z = q.popleft()

        if x == n-1 and y == m-1:
            return v[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if g[nx][ny] == 1 and v[nx][ny][1] == 0 and z == 0:
                v[nx][ny][1] = v[x][y][z] + 1
                q.append((nx, ny, 1))
            elif g[nx][ny] == 0 and v[nx][ny][z] == 0:
                v[nx][ny][z] = v[x][y][z] + 1
                q.append((nx, ny, z))

    return -1

print(bfs())
