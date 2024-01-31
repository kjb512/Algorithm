import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())

path = [list(map(int, input().split())) for _ in range(n)]

parent = [i for i in range(n + 1)]


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


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


for _ in range(m):
    q, w = map(int, input().split())
    union(q, w)


edges = []
for i in range(n):
    for j in range(i + 1, n):
        edges.append([dist(path[i][0], path[i][1], path[j][0], path[j][1]), i + 1, j + 1])

edges.sort()
res = 0
for cost, x, y in edges:
    if find(x) != find(y):
        union(x, y)
        res += cost

print(format(res, '.2f'))
