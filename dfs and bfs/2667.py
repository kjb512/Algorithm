# global count 몰랐음, 오름차순 정령 문제 똑바로 읽기, bfs 풀이도 보기
n = int(input())

g = []

for i in range(n):
    g.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if g[x][y] == 1:
        global count
        count += 1
        g[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
counter = []
count = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            counter.append(count)
            result += 1
            count = 0

print(result)
counter.sort()
for i in counter:
    print(i)
