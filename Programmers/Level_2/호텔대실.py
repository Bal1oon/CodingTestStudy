# https://school.programmers.co.kr/learn/courses/30/lessons/155651

import heapq

def solution(book_time):
    times = []
    for start, end in book_time:
        start_min = to_minute(start)
        end_min = to_minute(end) + 10
        times.append((start_min, end_min))
        
    times.sort()
    
    heap = []
    for start, end in times:
        if heap and heap[0] <= start:
            h = heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)

def to_minute(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m