import sys, heapq, collections

input = sys.stdin.readline

t = int(input())
for a in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    d = collections.defaultdict(int)
    for _ in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            d[n] += 1
        else:
            if n == 1:
                while max_heap:
                    num = -heapq.heappop(max_heap)
                    if d[num] > 0:
                        d[num] -= 1
                        break
            else:
                while min_heap:
                    num = heapq.heappop(min_heap)
                    if d[num] > 0:
                        d[num] -= 1
                        break

    isE1 = True
    isE2 = True
    ma = 0
    mi = 0
    while max_heap:
        num = -heapq.heappop(max_heap)
        if d[num] > 0:
            isE1 = False
            ma = num
            break

    while min_heap:
        num = heapq.heappop(min_heap)
        if d[num] > 0:
            isE2 = False
            mi = num
            break

    if isE1 or isE2:
        print("EMPTY")
    else:
        print(ma, mi)
