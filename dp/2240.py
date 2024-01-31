import sys

input = sys.stdin.readline

t, w = map(int, input().split())

p = [0] + [int(input().strip())for _ in range(t)]

dp = [[0] * (w+1) for _ in range(t+1)]

for i in range(1, t+1):

    if p[i] == 1:
        dp[i][0] = dp[i-1][0]+1
    else:
        dp[i][0] = dp[i-1][0]

    for c in range(1, w+1):
        # 2번나무, 위치 2번
        if p[i] == 2 and c % 2 == 1:
            dp[i][c] = max(dp[i-1][c-1], dp[i-1][c]) + 1
        # 1번 나무, 위치 1번
        elif p[i] == 1 and c % 2 == 0:
            dp[i][c] = max(dp[i-1][c-1], dp[i-1][c]) + 1
        # 위치가 다름
        else:
            dp[i][c] = max(dp[i-1][c-1], dp[i-1][c])


print(max(dp[t]))