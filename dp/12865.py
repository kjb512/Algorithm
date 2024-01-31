import sys

input = sys.stdin.readline

n, k = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(k+1)]for _ in range(n+1)]

for i in range(1, n+1):
    w, v = item[i-1]
    for j in range(1, k+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])