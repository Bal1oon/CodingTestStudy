import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)

if n == 1:
    print(0)
else:
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        total += a + b
        heapq.heappush(heap, a + b)
    print(total)