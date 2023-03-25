import math

n = int(input())


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

a = [False, False] + [True] * (n-1)
prime = []
# 소수 찾기(에라토스테네스의 체)
for i in range(2, n+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

# 연속 합 구하기
s = 0
e = 0
res = 0

while e <= len(prime):
    now = sum(prime[s:e])
    if now == n:
        res += 1
        s += 1
    elif now < n:
        e += 1
    else:
        s += 1

print(res)