import sys

input = sys.stdin.readline

n = int(input().strip())
s = [int(input().strip()) for _ in range(n)]

dp = [[0 for _ in range(2)]for _ in range(n+1)]

if n > 0:
    dp[1][0] = s[0]
    dp[1][1] = s[0]

if n > 1:
    dp[2][0] = dp[1][1] + s[1]
    dp[2][1] = s[1]

for i in range(3, n+1):
    dp[i][0] = dp[i-1][1] + s[i-1]
    dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + s[i-1]

print(max(dp[n]))
