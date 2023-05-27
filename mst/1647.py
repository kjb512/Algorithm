import sys

input = sys.stdin.readline

v,e = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(e)]

parent = [i for i in range(v+1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges.sort(key=lambda x:x[2])

total = 0
m = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a,b)
        total += cost
        m = max(m, cost)

print(total-m)