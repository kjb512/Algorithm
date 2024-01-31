import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

max_heap = []
min_heap = []
mid = 0

for i in range(n):
    num = int(input())

    if len(max_heap) == len(min_heap):
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)

    if min_heap and min_heap[0] < -max_heap[0]:
        leftValue = heappop(max_heap)
        rightValue = heappop(min_heap)

        heappush(max_heap, -rightValue)
        heappush(min_heap, -leftValue)


    print(-max_heap[0])