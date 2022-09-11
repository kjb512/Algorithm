# 럭키 스트레이트

s = list(map(int, input()))

l = r = 0

for i in range(len(s)):
    if i < len(s)/2:
        l += s[i]
    else:
        r += s[i]

if l == r:
    print("LUCKY")
else:
    print("READY")
# 피드백
# 정수 각자리수로 나누기 몰랐음