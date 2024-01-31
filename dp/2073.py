import sys

input = sys.stdin.readline

d, p = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(p)]

dp = [[0 for _ in range(d+1)] for _ in range(p+1)]

for i in range(1, p+1):
    le, v = l[i-1]
    for j in range(1, d+1):
        if j == le:
            dp[i][j] = max(dp[i-1][j], v)
        elif j > le:
            if dp[i - 1][j - le] > 0:
                dp[i][j] = max(min(dp[i][j-le], v), dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[p][d])