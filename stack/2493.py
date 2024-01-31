import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

res = [0] * n
s = []

for i in range(n):
    while s:
        a, idx = s.pop()
        if a >= l[i]:
            res[i] = idx
            s.append((a, idx))
            break
    s.append((l[i], i+1))

print(' '.join(map(str, res)))