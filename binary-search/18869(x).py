import sys
from collections import defaultdict
# 좌표 압축문제
input = sys.stdin.readline
m, n = map(int, input().split())
universe = defaultdict(int)
for _ in range(m):
    planet = list(map(int, input().split()))
    sorted_planet = sorted(list(set(planet)))
    rank = {sorted_planet[i]: i for i in range(len(sorted_planet))}
    vector = tuple([rank[i] for i in planet])
    universe[vector] += 1

print(sum(map(lambda x: x*(x-1)//2, universe.values())))