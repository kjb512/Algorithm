import sys

input = sys.stdin.readline

c, n = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(n)]

dp = [1e9 for _ in range(c+100)]
dp[0] = 0

for cost, benefit in l:
    for i in range(benefit, c+100):
        dp[i] = min(dp[i], dp[i-benefit] + cost)

print(min(dp[c:]))