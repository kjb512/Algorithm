import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.readline
a,b,c,d = [],[],[],[]
ab, cd = [],[]

n= int(input())
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp[0])
    b.append(tmp[1])
    c.append(tmp[2])
    d.append(tmp[3])

for i in range(n):
    for j in range(n):
        ab.append(a[i]+b[j])

for i in range(n):
    for j in range(n):
        cd.append(c[i]+d[j])


ab.sort()
cd.sort()
cnt = 0

# 이분탐색 시간초과..
# for i in ab:
#     target = -i
#     br = bisect_right(cd, target)
#     bl = bisect_left(cd, target)
#     cnt += br - bl


#투포인터
left = 0
right = len(cd) -1
while left < len(ab) and right >= 0:
    tmp = ab[left] + cd[right]
    if tmp == 0:
        next_left = left + 1
        next_right = right - 1
        while next_left < len(ab) and ab[next_left] == ab[left]:
            next_left += 1

        while next_right >= 0 and cd[next_right] == cd[right]:
            next_right -= 1
        cnt += (next_left-left) * (right-next_right)
        left, right = next_left, next_right

    elif tmp > 0:
        right -= 1
    else:
        left += 1

print(cnt)

# [-45, -41, -36, -36, -32, 26]
# [-54, -38, -27, -27, 30, 53]
# [-75, -37, 27, 27, 42, 56]
# [-46, -16, 30, 45, 62, 77]