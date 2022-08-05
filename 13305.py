city = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

m = max(cost)

sum = 0
for i in distance:
    sum += i

res = 0
for i in range(city-1):
    if(cost[i] < m):
        m = cost[i]
    res += m * distance[i]

print(res)
