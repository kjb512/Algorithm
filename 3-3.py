# n = 행 m = 열
n, m = map(int, input().split())

res = 0 
for i in range(n):
  data = list(map(int, input().split()))
  res= max(min(data), res)
  
print(res)