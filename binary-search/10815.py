n = int(input())
a = {}
for i in list(map(int, input().split())):
    a[i] = 1
m = int(input())
for j in list(map(int, input().split())):
    if j in a:
        print(1, end=' ')
    else:
        print(0, end=' ')
