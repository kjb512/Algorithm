import sys

input = sys.stdin.readline

n = int(input())

balance = list(map(int, input().split()))

j = int(input())

c = int(input())

tot_tickets = sum(balance)

kh = balance[0]

win_percentage = kh / tot_tickets

expect = win_percentage * j

print(kh+expect*c)