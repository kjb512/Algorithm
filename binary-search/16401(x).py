import sys

input = sys.stdin.readline

m,n = map(int, input().split())
l = list(map(int, input().split()))


def check(x):
    if x == 0:
        return True
    cnt = 0
    for i in l:
        cnt += i // x

    return cnt>= m

st = 1
en = max(l)
res = 0

while st <= en:
    mid = (st+en)//2

    if check(mid):
        st = mid + 1
        res = max(res, mid)
    else:
        en = mid - 1

print(res)
