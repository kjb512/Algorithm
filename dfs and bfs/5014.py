from collections import deque
f, s, g, u, d = map(int, input().split())

ud = [0] * 2
ud[0] += u
ud[1] -= d

v = [False] * (f+1)

def bfs(start, f, g, v, ud):
    q = deque()
    q.append((start, 0))
    v[start] = True

    while q:
        x , level = q.popleft()
        if x == g:
            return level

        for i in range(2):
            nx = x + ud[i]
            if 0 < nx <= f and not v[nx]:
                q.append((nx, level + 1))
                v[nx] = True

    return -1


res = bfs(s, f, g, v, ud)
if res == -1:
    print("use the stairs")
else:
    print(res)