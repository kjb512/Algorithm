import sys

l = []
cnt = 0
for line in sys.stdin:
    l.append([int(e) for e in line.split()])

dp = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(1001)]

s = len(l)

for i in range(s):
    for w in range(16):
        for b in range(16):
            if w < 15:
                dp[i+1][w+1][b] = max(dp[i+1][w+1][b], dp[i][w][b] + l[i][0])
            if b < 15:
                dp[i+1][w][b+1] = max(dp[i+1][w][b+1], dp[i][w][b] + l[i][1])
            dp[i+1][w][b] = max(dp[i+1][w][b], dp[i][w][b])

print(dp[s][15][15])