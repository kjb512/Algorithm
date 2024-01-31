import sys, itertools

input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
s = s + list(map(sum, itertools.combinations(s, 2)))

s.sort()
INF = 1e9
dp = [INF] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    for num in s:
        if num > i:
            break
        dp[i] = min(dp[i], dp[i-num] + 1)

print(dp[n]) if not dp[n] == INF else print(-1)