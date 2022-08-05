# 피로도
# a = 피로도 , b = 일 처리량 , c = -피로도 , m = 피로도 최대치
a, b, c, m = map(int, input().split())

# x = 일한 시간 , y = 휴식시간

piro = 0
work = 0

if(a > m):
    print(0)
else:
    for x in range(25):
        if(piro + a <= m):
            piro += a
            work += b
        else:
            if (piro - c >= 0):
                piro -= c
            else:
                piro = 0

print(work)
