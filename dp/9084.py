import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [1] + [0 for _ in range(target)]
    for coin in coins:
        for j in range(1, target + 1):
            if j-coin >=0:
                dp[j] += dp[j-coin]

    print(dp[target])