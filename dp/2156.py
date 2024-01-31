import sys

input = sys.stdin.readline

n = int(input().strip())
w = [int(input().strip())for _ in range(n)]

dp = [0] * (n)
dp[0] = w[0]
if n > 1:
  dp[1] = dp[0] + w[1]
if n > 2:
  dp[2] = max(w[0] + w[2], w[1] + w[2], dp[1])
for i in range(3, n):
  dp[i] = max(dp[i-2] + w[i], dp[i-3] + w[i-1] + w[i], dp[i-1])

print(dp[n-1])