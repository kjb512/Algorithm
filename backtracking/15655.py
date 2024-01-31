import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

arr = []
v = [False] * n

nums.sort()

def dfs(st):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(st, n):
        arr.append(nums[i])
        dfs(i+1)
        arr.pop()

dfs(0)