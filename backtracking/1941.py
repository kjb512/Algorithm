import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

g = [list(input().strip()) for _ in range(5)]

p = [(i, j) for i in range(5) for j in range(5)]

combs = combinations(p, 7)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

count = 0

for comb in list(combs):
    c = 0
    for x, y in comb:
        if g[x][y] == 'Y':
            c += 1
    if c > 3:
        continue

    visited = [False] * 7
    q = deque()
    q.append(comb[0])
    visited[0] = True

    v = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in comb:
                ni = comb.index((nx, ny))
                if not visited[ni]:
                    v += 1
                    visited[ni] = True
                    q.append((nx, ny))

    if v == 6:
        count += 1

print(count)
