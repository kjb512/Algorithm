import sys

test = int(input())

for a in range(test):
    num = int(input())
    score = []
    for i in range(num):
        score1, score2 = map(int, sys.stdin.readline().split())
        score.append([score1, score2])

    score.sort()

    m = score[0][1]

    count = 1
    for i in range(1, num):
        if(score[i][1] < m):
            m = score[i][1]
            count += 1
    print(count)
