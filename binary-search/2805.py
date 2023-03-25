import sys
input = sys.stdin.readline

N, M = map(int, input().split())

l = list(map(int, input().split()))


def check(x):
    if x == 0:
        return True

    m = 0

    for i in l:
        if i > x:
            m += i-x

    return m >= M


st = 0
en = max(l)
while st < en:
    mid = (st + en + 1) // 2
    if check(mid):
        st = mid
    else:
        en = mid - 1

print(st)
