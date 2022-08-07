n = list(map(int, input()))

n.sort(reverse=True)

if(n[-1] != 0):
    print(-1)
else:
    res = 0
    for i in n:
        res += i % 3

    if(res % 3 != 0):
        print(-1)
    else:
        print(int(''.join(map(str, n))))
