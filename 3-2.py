# 배열의 크기, 숫자가 더해지는 횟수, 연속가능 횟수
n, m, k = map(int, input().split())

data = list(map(int,input().split()))

data.sort(reverse = True)

res = 0

if data[0] == data[1]:
    res = data[0]*m
else:
  for i in range(m):
    if i%(k + 1) == 1:
      res += data[1]
    else:
      res += data[0]

print(res)
