import sys


input = sys.stdin.readline

n, m = map(int, input().split())

d = {}
for i in range(n):
    s = input().rstrip()
    d[i+1] = s
    d[s] = i+1

for i in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(d[int(q)])
    else:
        print(d[q])