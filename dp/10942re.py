import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
m = int(input())
q = [list(map(int, input().split())) for _ in range(m)]
isPalindrome = [[False]*(n+2) for _ in range(n+2)]

for i in range(1, n+1):
    isPalindrome[i][i] = True
    if i == n: break
    isPalindrome[i][i+1] = l[i-1] == l[i]

for i in range(3, n+1):
    for j in range(1, i-1):
        isPalindrome[j][i] = isPalindrome[j+1][i-1] and l[j-1] == l[i-1]

for s, j in q:
    print(1) if isPalindrome[s][j] else print(0)