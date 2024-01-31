import sys

input = sys.stdin.readline

n = int(input().strip())

parent = [i for i in range(n+1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(i, n):
        edges.append([tmp[j], i , j])

edges.sort()

res = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a,b)
        res += cost

print(res)