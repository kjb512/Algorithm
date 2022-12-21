import sys

# 새롭게 알게된점: pypy3는 재귀에 약함으로 bfs를 사용하자. c++도 같이 준비하는게 좋아보인다.
sys.setrecursionlimit(10**4)
# 입력
n, m = map(int, sys.stdin.readline().strip().split())

g = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x < 0 or x > n or y < 0 or y > m:
        return False
    if g[x][y] == 0:
        return False
    if v[x][y] == 0:
        # 방문하고, 녹는 얼음이 없는 경우: -1, 녹는 얼음이 있는 경우: 녹는 얼음의 개수
        v[x][y] = -1
        melt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n or ny < 0 or ny > m:
                continue
            if g[nx][ny] == 0:
                melt += 1
                continue
            dfs(nx, ny)
        if melt > 0:
            v[x][y] = melt
        return True
    return False

year = 0
while True:
    cnt = 0

    # 방문 기록 + 녹는 얼음 count
    v = [[0 for _ in range(m)] for _ in range(n)]
    # 덩어리 계산, 녹는 얼음 세기
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                cnt += 1

    # 녹이기
    for i in range(n):
        for j in range(m):
            if v[i][j] > 0:
                g[i][j] -= v[i][j]
                if g[i][j] < 0:
                    g[i][j] = 0

    if cnt == 0:
        print(0)
        exit()
    if cnt > 1:
        print(year)
        exit()

    year += 1