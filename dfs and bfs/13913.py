import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

M = 100001

v = [-1] * M

q = deque()
q.append((n, 0))
v[n] = 0
ans = []

while q:
    cur, cnt = q.popleft()
    if cur == k:
        print(cnt)
        for _ in range(cnt):
            ans.append(cur)
            cur = v[cur]
        ans.append(cur)
        break
    nx1 = cur - 1
    nx2 = cur + 1
    nx3 = cur * 2
    if 0 <= nx1 and v[nx1] == -1:
        q.append((nx1, cnt+1))
        v[nx1] = cur
    if nx2 < M and v[nx2] == -1:
        q.append((nx2, cnt+1))
        v[nx2] = cur
    if nx3 < M and v[nx3] == -1:
        q.append((nx3, cnt+1))
        v[nx3] = cur


ans.reverse()

print(*ans)