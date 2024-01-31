import sys
from collections import deque
from heapq import heappop, heappush

input = sys.stdin.readline

n, k = map(int, input().split())
# bfs 풀이
# m = 100000
#
# v = [0 for _ in range(m + 1)]
#
# q = deque()
# q.append((n, 0))
# while q:
#     cur, level = q.popleft()
#     if cur is k:
#         print(level)
#         break
#
#     for nex, n_lev in [(cur * 2, level), (cur - 1, level + 1), (cur + 1, level + 1)]:
#         if 0 <= nex <= m and v[nex] == 0:
#             v[nex] = 1
#             q.append((nex, n_lev))

# dijkstra 풀이
INF = 1e9
d = [INF] * (100001)
q = []
def dijkstra(start):
    d[start] = 0
    heappush(q, (0, start))

    while q:
        dist, node = heappop(q)

        if d[node] < dist:
            continue
        for n_node, nd in [(node * 2, 0), (node - 1, 1), (node + 1, 1)]:
            cost = dist + nd
            if 0 <= n_node <= 100000 and cost < d[n_node]:
                d[n_node] = cost
                heappush(q,(cost, n_node))

dijkstra(n)
print(d[k])