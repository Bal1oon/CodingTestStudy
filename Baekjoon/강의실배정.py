# https://www.acmicpc.net/problem/11000

import heapq
import sys

input = sys.stdin.readline

n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]
lectures.sort()

heap = []
heapq.heappush(heap, lectures[0][1])
for i in range(1, n):
    if lectures[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, lectures[i][1])
print(len(heap))