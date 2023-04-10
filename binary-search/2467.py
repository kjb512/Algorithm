import sys

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))



left = 0
right = 0
res = float("INF")

for i in range(n-1):
    st = i + 1
    en = n - 1
    while st <= en:
        mid = (st+en) // 2
        a = l[i] + l[mid]
        if abs(a) < res:
            res = abs(a)
            left = l[i]
            right = l[mid]

            if sum == 0:
                break

        if a < 0:
            st = mid + 1
        else:
            en = mid - 1


print(left, right)


