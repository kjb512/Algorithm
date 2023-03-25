from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
d = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def naming(a, b):
    q = deque()
    q.append((a, b))
    g[a][b] = name

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] == 1:
                    g[nx][ny] = name
                    q.append((nx, ny))


def sol(a, b):
    q = deque()
    q.append((a, b))
    d[a][b] = 1

    while q:
        x, y = q.popleft()

        if d[x][y] >= ans:
            return 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] == 0:
                    if d[nx][ny] == 0 or d[nx][ny] > d[x][y] + 1:
                        d[nx][ny] = d[x][y] + 1
                        q.append((nx, ny))
                elif g[nx][ny] != end:
                    return d[x][y]

    return 0


def isEnd(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if g[nx][ny] != 0:
                return g[nx][ny]

    return -1


# 대륙간 식별자 부여
name = 2
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            naming(i, j)
            name += 1

ans = n * n
for i in range(n):
    for j in range(n):
        if g[i][j] == 0:
            end = isEnd(i, j)
            if end != -1:
                res = sol(i, j)
                if res != 0:
                    ans = res

print(ans)