import sys
import bisect

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))

l.sort()
cnt = 0
for i in range(n):
    tmp = l[:i] + l[i+1:]
    li = 0
    ri = n-2
    while li < ri:
        a = tmp[li] + tmp[ri]
        if a == l[i]:
            cnt += 1
            break
        elif a < l[i]:
            li += 1
        else:
            ri -= 1
print(cnt)
