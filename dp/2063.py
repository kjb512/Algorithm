import sys

input = sys.stdin.readline

d,p = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(p)]

dp = [[0 for _ in range(d+1)] for _ in range(p+1)]

for i in range(1, p+1):
    length, v = l[p-1]
    for j in range(1, d+1):
        if j - length >= 0:
            dp[i][j] = dp[i-1][p-j]



print(l)