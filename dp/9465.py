import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())

    score = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * 2 for _ in range(n+1)]
    dp[1][0] = score[0][0]
    dp[1][1] = score[1][0]
    if n > 1:
        dp[2][0] = dp[1][1] + score[0][1]
        dp[2][1] = dp[1][0] + score[1][1]

    for i in range(3, n+1):
        dp[i][0] = max(dp[i-1][1] + score[0][i-1], dp[i-2][1] + score[0][i-1])
        dp[i][1] = max(dp[i-1][0] + score[1][i-1], dp[i-2][0] + score[1][i-1])
    print(max(dp[n]))