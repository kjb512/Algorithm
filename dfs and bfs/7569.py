from collections import deque
# m: 상자의 가로, n: 상자의 세로, h: 상자의 높이
m, n, h = map(int, input().split())

# b: box
b = [[[] for _ in range(n)] for _ in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        b[i][j] = list(map(int, input().split()))
        for k in range(m):
            if b[i][j][k] == 1:
                queue.append((i, j, k))

direction = [(1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0)]

# 출력: 안익는 경우, 익으면 몇일이 걸리는지..
# 악익으려면 어떤 경우에 안익는가? : 안익은 무리들 주변이 비어있을 경우

res = 0

while queue:
    qh, qn, qm = queue.popleft()
    for i in range(6):
        dh = qh + direction[i][0]
        dn = qn + direction[i][1]
        dm = qm + direction[i][2]
        if 0 <= dh < h and 0 <= dn < n and 0 <= dm < m and b[dh][dn][dm] == 0:
            b[dh][dn][dm] = b[qh][qn][qm] + 1
            queue.append((dh, dn, dm))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if b[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                res = max(res, b[i][j][k])
print(res-1)