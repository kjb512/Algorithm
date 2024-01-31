import sys

input = sys.stdin.readline

n = int(input().strip())
card = list(map(int, input().split()))

dp = [0]*(n+1)
dp[1] = card[0]


for i in range(2, n+1):
    m = card[i-1]
    for j in range(1, i):
        m = max(m, dp[i-j] + card[j-1])
    dp[i] = m

print(dp[n])