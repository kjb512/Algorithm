import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

l.sort()

# [-97, -6, -2, 6, 98]
res_sum = float("INF")
res_f = 0
res_s = 0
res_t = 0
for i in range(n-1):
    for j in range(i+1, n):
        tmp = l[i] + l[j]
        st = j + 1
        en = n - 1
        while st <= en:
            mid = (st+en)//2
            fin = l[mid] + tmp
            if res_sum > abs(fin):
                res_sum = abs(fin)
                res_f = l[i]
                res_s = l[j]
                res_t = l[mid]
            if fin == 0:
                break
            elif fin > 0:
                en = mid - 1
            else:
                st = mid + 1

print(res_f,res_s,res_t)