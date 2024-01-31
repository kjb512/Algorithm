import sys

input = sys.stdin.readline

r, c, w = map(int, input().split())

dp = [[0 for _ in range(r+w-1)]for _ in range(r+w-1)]

for i in range(r+w-1):
    for j in range(i+1):
        if i == j:
            dp[i][j]= 1
            break

        if j==0:
            dp[i][j]= 1
            continue

        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

sum = 0
for i in range(w):
    for j in range(i+1):
        sum += dp[r-1+i][c-1+j]

print(sum)
