import sys, copy

input = sys.stdin.readline

# 입력
n, m, t = map(int, input().split())
sector = list(map(int, input().split()))
p = int(input())

tot = m-sector[p-1]
# 0 이상일 경우
if tot > 0:
    dp = [[0 for _ in range(tot+1)] for _ in range(n+2)]

    # 왼쪽 knapsack 알고리즘
    for i in range(1, p):
        group = sector[i-1]
        for j in range(1, tot+1):
            temp = j-group
            if temp >= 0:
                if temp == 0:
                    dp[i][j] = p-i
                else:
                    if dp[i-1][temp] > 0:
                        if dp[i-1][j] > 0:
                            dp[i][j] = min(dp[i-1][j], dp[i-1][temp])
                        else:
                            dp[i][j] = dp[i-1][temp]
                    else:
                        dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    # 오른쪽 knapsack 알고리즘
    for i in range(n, p, -1):
        group = sector[i-1]
        for j in range(1, tot+1):
            temp = j-group
            if temp >= 0:
                if temp == 0:
                    dp[i][j] = i-p
                else:
                    if dp[i+1][temp] > 0:
                        if dp[i+1][j] > 0:
                            dp[i][j] = min(dp[i+1][j], dp[i+1][temp])
                        else:
                            dp[i][j] = dp[i+1][temp]
                    else:
                        dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = dp[i+1][j]

    # 오른쪽 왼쪽 합치기
    INF = 1e9
    res = INF
    for i in range(1, tot):
        if dp[p-1][i] > 0 and dp[p+1][tot-i] > 0:
            l, r = dp[p-1][i], dp[p+1][tot-i]
            res = min(res, min(l,r)*2 + max(l,r))

    # 오른쪽 왼쪽 단일 경우
    if dp[p-1][tot] > 0:
        res = min(res, dp[p-1][tot])
    if dp[p+1][tot] > 0:
        res = min(res, dp[p+1][tot])

    if res > t:
        print('NO')
    else:
        print('YES')
# 예외 처리
elif tot == 0 and m == sector[p-1]:
    print('YES')
else:
    print('NO')