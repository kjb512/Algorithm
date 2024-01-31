import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]



    for i in range(2, m+1):
        for j in range(2, n+1):
            if j == 2:
                dp[i][j] = i//2 + dp[i-1][j]
            else:
                dp[i][j] = dp[i//2][j-1] + dp[i-1][j]

    if n == 1:
        print(m)
    else:
        print(dp[m][n])
