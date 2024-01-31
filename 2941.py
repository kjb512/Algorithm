import sys

input = sys.stdin.readline

str = input().strip()

alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in alp:
    str = str.replace(a, '@')

print(len(str))