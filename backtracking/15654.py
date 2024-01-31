import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

arr = []
v = [False] * n

nums.sort()

def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(n):
        if not v[i]:
            v[i] = True
            arr.append(nums[i])
            dfs()
            arr.pop()
            v[i] = False


dfs()