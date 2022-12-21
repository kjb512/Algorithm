from collections import deque
t = int(input())

h = []
s = [[] for _ in range(t)]
sv = [[] for _ in range(t)]
g = []

# 입력
for i in range(t):
    sn = int(input())
    hx, hy = map(int, input().split())
    h.append((hx, hy))
    for j in range(sn):
        sx, sy = map(int, input().split())
        s[i].append((sx, sy))
        sv[i].append(False)
    gx, gy = map(int, input().split())
    g.append((gx, gy))

def d(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def bfs(start, s, g, sv):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        if d(x, y, g[0], g[1]) <= 1000:
            return True

        for i in range(len(s)):
            if d(x, y, s[i][0], s[i][1]) <= 1000 and not sv[i]:
                q.append((s[i][0], s[i][1]))
                sv[i] = True


    return False


for i in range(t):
    if bfs(h[i], s[i], g[i], sv[i]):
        print("happy")
    else:
        print("sad")