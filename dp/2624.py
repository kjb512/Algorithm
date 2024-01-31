import sys

input = sys.stdin.readline

t = int(input())
k = int(input())

dp = [0 for _ in range(t+1)]
dp[0] = 1

for _ in range(k):
    coin, cnt = map(int, input().split())
    for i in range(t, 0, -1):
        for j in range(1, cnt+1):
            if i - coin*j < 0:
                continue
            dp[i] += dp[i-coin*j]


print(dp[t])