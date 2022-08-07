a, b = map(int, input().split())

count = 0
while True:
    if(b == 0):
        count = -1
        break
    elif(a == b):
        count += 1
        break
    elif(b % 2 == 0):
        count += 1
        b //= 2
    elif(b > 10 and (b-1) % 10 == 0):
        count += 1
        b = (b-1)//10
    else:
        count = -1
        break

print(count)
