import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n, m = map(int, input().split())

    ap = [list(map(int, input().split()))for _ in range(m)]

    parent = [i for i in range(n+1)]

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])

        return parent[a]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[a] = b
        else:
            parent[b] = a

    count = 0
    for a, b in ap:
        if find(a) != find(b):
            union(a, b)
            count += 1

    print(count)
