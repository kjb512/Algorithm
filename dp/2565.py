import sys, bisect

input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

l.sort()
dp = []
size = 0
for a, b in l:
    i = bisect.bisect_left(dp, b)
    if i == size:
        dp.append(b)
        size += 1
    else:
        dp[i] = b

print(n-size)