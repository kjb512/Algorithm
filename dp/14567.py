import sys

input = sys.stdin.readline

n, m = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(m)]

dp = [1 for _ in range(n+1)]

l.sort()

for a, b in l:
    dp[b] = max(dp[b], dp[a] + 1)

print(' '.join(map(str, dp[1:])))