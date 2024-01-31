import sys


input = sys.stdin.readline

n = int(input().strip())

visited1 = [False] * (40)
visited2 = [False] * (40)
visited3 = [False] * (40)

count = 0


def dfs(cur):
    if cur == n:
        global count
        count += 1
        return

    for i in range(n):
        if visited1[i] or visited2[cur - i + n - 1] or visited3[cur + i]:
            continue
        visited1[i] = True
        visited2[cur - i + n - 1] = True
        visited3[cur + i] = True
        dfs(cur + 1)
        visited1[i] = False
        visited2[cur - i + n - 1] = False
        visited3[cur + i] = False


dfs(0)

print(count)
