import sys
input = sys.stdin.readline

m, n = map(int, input().split())

a = list(map(int, input().split()))

def check(x):
    if x == 0:
        return True
    cnt = 0

    for i in a:
        cnt += i // x

    return cnt >= m

st = 0
en = max(a)

while st < en:
    mid = (st + en + 1) // 2
    if check(mid):
        st = mid
    else:
        en = mid - 1

print(st)