from collections import deque
n = int(input())

g = [list(map(int, input().split())) for _ in range(n)]

v = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, g, v, h):
    q = deque()
    q.append(start)
    v[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not v[nx][ny] and g[nx][ny] > h:
                    q.append((nx, ny))
                    v[nx][ny] = True

count = 0
max = 1
for i in range(101):
    v = [[False] * n for _ in range(n)]

    if max < count:
        max = count

    if max > 1 and count == 0:
        break

    count = 0
    for j in range(n):
        for k in range(n):
            if g[j][k] > i and not v[j][k]:
                bfs((j, k), g, v, i)
                count += 1

print(max)