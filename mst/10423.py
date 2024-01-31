import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

plant = list(map(int, input().split()))

cables = [list(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n+1)]

for i in plant:
    parent[i] = 0

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b



cables.sort(key=lambda x: x[2])
res = 0
for a, b, cost in cables:
    if find(a) != find(b):
        union(a, b)
        res += cost

print(res)