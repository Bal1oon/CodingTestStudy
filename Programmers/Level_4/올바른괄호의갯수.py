# https://school.programmers.co.kr/learn/courses/30/lessons/12929#

def solution(n):
    d = [0] * (n+1)
    d[0], d[1] = 1, 1
    
    for i in range(2, n+1):
        for j in range(i):
            d[i] += d[j] * d[i-1-j]
    
    return d[-1]