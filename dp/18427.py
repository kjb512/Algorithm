import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(n)]

dp = [0for _ in range(h+1)]
dp[0] = 1

for i in range(n):
    for j in range(h, 0, -1):
       for num in l[i]:
           if j-num < 0:
               continue
           dp[j] += dp[j-num]

print(dp[h]%10007)