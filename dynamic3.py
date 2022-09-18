# 개미 전사

n = int(input())

f = list(map(int, input().split()))

d = [0] * 100

d[0] = f[0]
d[1] = max(f[0], f[1])


for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + f[i])

print(d[n-1])