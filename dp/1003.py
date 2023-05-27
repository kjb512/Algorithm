import sys

input = sys.stdin.readline

t = int(input())
n = []


for _ in range(t):
    n.append(int(input()))


dp = [[0,0] for _ in range(max(n)+2)]
dp[0] = [1,0]
dp[1] = [0,1]

res = []

for num in n:

    if num == 0:
        print(1,0)
        continue

    if num == 1:
        print(0,1)
        continue

    for i in range(2, num+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

    print(dp[num][0], dp[num][1])

