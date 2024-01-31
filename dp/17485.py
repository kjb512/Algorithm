import sys

input = sys.stdin.readline

n, m = map(int, input().split())

path = [list(map(int, input().split())) for _ in range(n)]

INF = 1e9

dp = [[[INF for _ in range(3)] for _ in range(m)] for _ in range(n)]

for i in range(m):
    for j in range(3):
        dp[0][i][j] = path[0][i]

for i in range(1, n):
    for j in range(m):
        for k in range(3):
            if (j == 0 and k == 2) or (j == m - 1 and k == 0):
                continue
            if k == 0:
                dp[i][j][k] = min(dp[i-1][j+1][1],dp[i-1][j+1][2]) + path[i][j]
            elif k == 1:
                dp[i][j][k] = min(dp[i-1][j][0], dp[i-1][j][2]) + path[i][j]
            else:
                dp[i][j][k] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + path[i][j]

res = min(min(dp[n - 1][j]) for j in range(m))

print(res)
