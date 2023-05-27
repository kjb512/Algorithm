import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]

tmp = 0
for i in range(n):
    t, p = map(int, input().split())
    tmp = max(tmp, dp[i])
    if i+t > n:
        continue
    dp[i+t] = max(dp[i+t], tmp + p)

print(dp)
print(max(dp))