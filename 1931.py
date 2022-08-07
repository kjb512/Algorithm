n = int(input())

t = []
for i in range(n):
    t.append(list(map(int, input().split())))

t.sort()
t.sort(key=lambda x: x[1])

m = t[0][1]

count = 1
for j in range(1, len(t)):
    if(t[j][0] >= m):
        m = t[j][1]
        count += 1

print(count)
