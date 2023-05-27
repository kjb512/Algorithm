import sys
import math

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+3)]
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, n+1):
    d = int(math.sqrt(i))
    mi = n
    for j in range(1, d+1):
        mi = min(mi, 1+dp[i - j*j])

    dp[i] = mi

print(dp[n])
