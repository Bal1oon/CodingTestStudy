# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    count = sorted(count.values(), reverse = True)
    num, sizes = 0, 0
    
    for c in count:
        num += c
        sizes += 1
        if num >= k:
            break
    
    return sizes