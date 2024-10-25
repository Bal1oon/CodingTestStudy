# https://school.programmers.co.kr/learn/courses/15009/lessons/121688

import heapq

def solution(ability, number):
    heapq.heapify(ability)
    
    for _ in range(number):
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)
        heapq.heappush(ability, a + b)
        heapq.heappush(ability, a + b)
    
    return sum(ability)