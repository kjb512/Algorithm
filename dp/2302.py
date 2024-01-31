import sys

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

v = [int(input().strip())for _ in range(m)]

dp = [0] * (41)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, n-m+1):
    dp[i] = dp[i-2] + dp[i-1]

prev = 1
res = 1
for vip in v:
    num = vip - prev
    res *= dp[num]
    prev = vip + 1

if prev < n:
    res *= dp[n+1 - prev]

print(res)