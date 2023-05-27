import sys

input = sys.stdin.readline


def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(e)]

parent = [i for i in range(v + 1)]

edges.sort(key=lambda x: x[2])
total = 0
for a,b,cost in edges:
    if find(parent, a) != find(parent,b):
        union(parent, a, b)
        total += cost

print(total)
