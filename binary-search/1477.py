import sys

input = sys.stdin.readline

n, m, l = map(int, input().split())
p = list(map(int, input().split()))

p.append(0)
p.append(l)

p.sort()

st = 0
en = l
res = 0
while st < en:
    cnt = 0
    mid = (st+en) // 2
    for i in range(n+1):
        now = p[i]
        while now + mid < p[i+1]:
            if cnt > m:
                break
            cnt += 1
            now += mid

    if cnt <= m:
        res = mid
        en = mid
    else:
        st = mid + 1

print(res)