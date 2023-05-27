import sys

input = sys.stdin.readline

n = int(input().strip())

parent = [i for i in range(n+1)]

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

W = [int(input().strip()) for _ in range(n)]
edges = []
for j in range(n):
    tmp = list(map(int, input().split()))
    for i in range(j+1, n):
        edges.append((tmp[i], j, i))

for i, w in enumerate(W):
    edges.append((w, i, n))

edges.sort()

total = 0
for cost, a,b in edges:
    if find(a) != find(b):
        union(a,b)
        total += cost

print(total)
