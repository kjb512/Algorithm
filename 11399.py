n = int(input())
t = []
t = list(map(int, input().split()))
t.sort()
sum = 0
wait = 0
for time in t:
    sum += wait + time
    wait += time
print(sum)
