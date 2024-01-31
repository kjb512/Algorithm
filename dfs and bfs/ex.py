

dp = [[0] for _ in range(len(transaction))]
now = 0
for t in transaction:
    md1 = max(dp[now])
    if md1 + t > 0:
        now += 1
        dp[now].append(md1+t)
    elif now != 0:
        md2 = max(dp[now - 1])
        if md2 + t > 0:
            dp[now].append(md2)