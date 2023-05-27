import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

dp = l[:]
for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + l[i])

dp.sort()

print(dp[n-1])