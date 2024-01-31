import sys

input = sys.stdin.readline

n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

tmp = 0
for i in range(n):
    t, p = l[i]
    tmp = max(dp[i], tmp)
    if i + t > n:
        continue
    dp[i+t] = max(dp[i+t], tmp+p)

print(max(dp))