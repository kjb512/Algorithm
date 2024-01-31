import sys

input = sys.stdin.readline

n, m = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

question = [list(map(int, input().split())) for _ in range(k)]

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] + l[i][j] - dp[i][j]

for x1, y1, x2, y2 in question:
    res = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(res)