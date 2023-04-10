import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

l.sort()
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        tmp = l[i] + l[j]
        target = 0
        target -= tmp
        bl = bisect_left(l[j+1:], target)
        br = bisect_right(l[j+1:], target)
        ans += br - bl

print(ans)
# [-6, -5, -4, -4, 0, 1, 2, 2, 3, 7]
# 이경우 시간 초과