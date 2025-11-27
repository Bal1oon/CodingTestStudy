# https://school.programmers.co.kr/learn/courses/30/lessons/161988

def solution(sequence):
    n = len(sequence)
    
    d1 = [0] * n
    d2 = [0] * n
    
    d1[0] = sequence[0]
    d2[0] = -sequence[0]
    
    for i in range(1, n):
        if i % 2 == 0:
            d1[i] = max(d1[i-1] + sequence[i], sequence[i])
            d2[i] = max(d2[i-1] - sequence[i], -sequence[i])
        else:
            d1[i] = max(d1[i-1] - sequence[i], -sequence[i])
            d2[i] = max(d2[i-1] + sequence[i], sequence[i])

    return max(max(d1), max(d2))