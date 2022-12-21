from collections import deque

n, k = map(int, input().split())

MAX = 10**5
arr = [0] * (MAX+1)


def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(arr[x])
            break

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not arr[nx]:
                arr[nx] = arr[x] +1
                q.append(nx)

bfs()