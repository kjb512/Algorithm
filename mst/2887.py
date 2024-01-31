import sys

input = sys.stdin.readline

n = int(input().strip())

planet = []

for i in range(n):
    planet.append(list(map(int, input().split())) + [i])

tunnels = []
for i in range(3):
    planet.sort(key=lambda x: x[i])
    for j in range(1, n):
        tunnels.append((abs(planet[j-1][i] - planet[j][i]), planet[j-1][3], planet[j][3]))

parent = [i for i in range(n)]

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

tunnels.sort()
res = 0
for cost, a, b in tunnels:
    if find(a) != find(b):
        union(a, b)
        res += cost

print(res)