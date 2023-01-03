import sys

def sol(start):
    i = start
    while True:
        v[i] = start
        i = g[i] - 1

        # 사이클이다.
        if v[i] == start:
            while v[i] != -1:
                v[i] = -1
                i = g[i] - 1
            return
        elif v[i] != -2:
            return




T = int(input())

for _ in range(T):

    n = int(sys.stdin.readline())
    g = list(map(int, sys.stdin.readline().split()))
    v = [-2 for _ in range(n)]

    for i in range(n):
        if v[i] == -2:
            sol(i)

    res = 0
    for i in range(n):
        if v[i] != -1:
            res += 1
    print(res)