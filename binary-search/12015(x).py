import sys
import bisect

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))

dp = [l[0]]

for num in l:
    if dp[-1] < num:
        dp.append(num)
    else:
        idx = bisect.bisect_left(dp, num)
        dp[idx] = num

print(len(dp))
