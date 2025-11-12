# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    times = 0
    removed = 0
    
    while s != '1':
        removed += s.count('0')
        s = bin(s.count('1'))[2:]
        times += 1
        
    return [times, removed]