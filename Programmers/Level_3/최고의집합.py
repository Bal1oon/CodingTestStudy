# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if n > s:
        return [-1]
    
    q, r = s // n, s % n
    answer = [q for _ in range(n-r)] + [q+1 for _ in range(r)]
    return answer

# -----------------------------
def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    if s % n == 0:
        answer = [s//n] * n
    else:
        answer = [s//n] * n
        for i in range(1, s%n + 1):
            answer[-i] += 1
    
    return answer