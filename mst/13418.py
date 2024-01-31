import sys

input = sys.stdin.readline

n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m+1)]

edges.sort(key=lambda x: x[2])

parent = [i for i in range(n+1)]

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

best = 0
worst = 0

up = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a,b)
        if cost == 0:
            up += 1

worst = up*up

edges.reverse()
parent = [i for i in range(n+1)]
up = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a,b)
        if cost == 0:
            up += 1
best = up*up


print(worst - best)
