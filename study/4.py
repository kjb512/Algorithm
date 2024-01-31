import sys

input = sys.stdin.readline

coin = float(input())

n = int(input())

problem = list(map(int, input().split()))

freeze = 0.99

count = int(coin // freeze)

count = min(count, 2)

dp = [[0 for _ in range(count+1)]for _ in range(n+1)]

m = 0
res = 0
for i in range(1, n+1):
    for j in range(count+1):
        m = max(problem[i-1], m)
        if problem[i-1] == 0:
            if j == 0:
                dp[i][0] = 0
            else:
                dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = dp[i-1][j] + 1
        res = max(res, dp[i][j])


print(res)
print(m)