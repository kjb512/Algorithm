import sys

input = sys.stdin.readline

n, m= map(int, input().split())

g = [list(map(int, input().strip())) for _ in range(n)]

res = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            res = max(res, g[i][j])
            continue
        if g[i][j] == 1:
            g[i][j] = min(g[i-1][j-1], g[i-1][j], g[i][j-1]) + 1
        res = max(res, g[i][j])

print(res**2)