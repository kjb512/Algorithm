import sys

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))

li = 0
ri = n - 1

ans = 1e9
while li < ri:
    tmp = l[li] + l[ri]
    if abs(tmp) < abs(ans):
        ans = tmp
    if tmp < 0:
        li += 1
    else:
        ri -= 1

print(ans)