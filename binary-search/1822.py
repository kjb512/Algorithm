nA, nB = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A - B))  # 차집합의 길이를 출력
print(*sorted(list(A - B)))  # 차집합의 원소를 출력
# 여기서 *은 unpacking 할때 사용됨.

# ----딕셔너리로 풀었을 경우----
a, b = map(int, input().split())
A, B = {}, {}
for n in map(int, input().split()):
    A[n] = 1
for n in map(int, input().split()):
    B[n] = 1

print(A)
print(B)

# 리스트로 풀면 시간초과가 나지만 해쉬로 풀면 문제를 해결할 수 있다.
C = []
for i in A:
    if i not in B:
        C += [i]

print(len(C))
print(*sorted(C))