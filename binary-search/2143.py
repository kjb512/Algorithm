import sys
import bisect

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

sa, sb = a, b
for i in range(n):
    for j in range(i + 1, n):
        sa.append(sum(a[i:j+1]))

for i in range(m):
    for j in range(i + 1, m):
        sb.append(sum(b[i:j+1]))

sa.sort()
sb.sort()
cnt = 0
for num in sa:
    target = t - num
    l = bisect.bisect_left(sb, target)
    r = bisect.bisect_right(sb, target)
    cnt += r - l

print(cnt)