# 문자열 재정렬

a = list(input())

num = 0
s = []

for i in range(len(a)):
    if str(a[i]).isdigit():
        num += int(a[i])
    else:
        s.append(a[i])

s.sort()

s.append(num)

print(''.join(str(i) for i in s))

# 피드백
# 한줄 for문
# str(i) for i in s
# str은 join list는 append