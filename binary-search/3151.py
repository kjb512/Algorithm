import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

d = defaultdict(int)

l.sort()
for i in l:
    d[i] += 1

res = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        target = -(l[i] + l[j])
        if target >= l[j]:
            if target == l[j]:
                if d[target] > 1:
                    cnt = 0
                    for k in range(1, d[target]):
                        if j + k < n and l[j + k] == target:
                            cnt += 1
                        else:
                            break
                    res += cnt
            else:
                res += d[target]

print(res)

# 2 -5 2 3 -4 7 -4 0 1 -6
# -6 -5 -4 -4 0 1 2 2 3 7
