import sys

input = sys.stdin.readline
n = int(input())

a,b,c,d = [],[],[],[]

for i in range(n):
    A,B,C,D = map(int,input().split())
    a.append(A)
    b.append(B)
    c.append(C)
    d.append(D)

ab, cd = [], []

for i in range(n):
    for j in range(n):
        ab.append(a[i] + b[j])

for i in range(n):
    for j in range(n):
        cd.append(c[i] + d[j])
cnt = 0
ab.sort()
cd.sort()
left = 0
right = n*n - 1
while left < n*n and right >= 0:
    tmp = ab[left] + cd[right]
    if tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1
    else:
        nleft = left + 1
        nright = right - 1
        while nleft < n*n and ab[left] == ab[nleft]:
            nleft += 1

        while nright >= 0 and cd[right] == cd[nright]:
            nright -= 1
        cnt += (right - nright) * (nleft - left)
        left, right = nleft, nright

# left = 0
# right = len(cd) -1
# while left < len(ab) and right >= 0:
#     tmp = ab[left] + cd[right]
#     if tmp == 0:
#         next_left = left + 1
#         next_right = right - 1
#         while next_left < len(ab) and ab[next_left] == ab[left]:
#             next_left += 1
#
#         while next_right >= 0 and cd[next_right] == cd[right]:
#             next_right -= 1
#         cnt += (next_left-left) * (right-next_right)
#         left, right = next_left, next_right
#
#     elif tmp > 0:
#         right -= 1
#     else:
#         left += 1

print(cnt)

# -45 22 22 23
# -41 -22 -22 30   4



