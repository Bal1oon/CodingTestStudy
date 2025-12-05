# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from collections import Counter
from itertools import combinations

def solution(orders, course):
    cnt = Counter()
    
    orders = [''.join(sorted(o)) for o in orders]

    for c in course:
        for o in orders:
            cnt += Counter(combinations(o, c))

    answer = []

    for c in course:
        candidates = [(combo, freq) for combo, freq in cnt.items() if len(combo) == c]

        if not candidates:
            continue

        max_freq = max(freq for combo, freq in candidates)

        if max_freq < 2:
            continue

        for combo, freq in candidates:
            if freq == max_freq:
                answer.append(''.join(combo))

    answer.sort()
    return answer
