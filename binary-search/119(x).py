import sys

input = sys.stdin.readline

n, c = map(int, input().split())
g = [int(input()) for _ in range(n)]

g.sort()

st, en = 1, g[n-1] - g[0]
if n == 2:
    print(g[1] -g[0])
else:
    res = 0
    while st <= en:
        mid = (st+en) // 2

        count = 1
        tmp = g[0]
        for num in g:
            if num - tmp >= mid:
                tmp = num
                count += 1
        if count < c:
            en = mid - 1
        else:
            res = mid
            st = mid + 1

    print(res)