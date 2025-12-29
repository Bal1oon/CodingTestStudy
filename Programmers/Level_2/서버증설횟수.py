# https://school.programmers.co.kr/learn/courses/30/lessons/389479
def solution(players, m, k):
    n = 1                       # 현재 서버 수
    l = len(players)
    expire = [0] * (l + k)      # expire[t] = t시에 반납할 서버 수
    
    for t in range(l):
        # 1. 만료된 서버 반납
        n -= expire[t]
        # 2. 현재 서버가 감당 가능한 최대 유저 수
        capacity = n * m
        # 3. 서버 증설
        if players[t] >= capacity:
            need = players[t] - capacity
            add = need // m + 1
            
            n += add
            expire[t + k] += add

    return sum(expire)
