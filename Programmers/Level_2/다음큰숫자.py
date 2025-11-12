# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    num = bin(n).count('1')
    while True:
        n += 1
        if num == bin(n).count('1'):
            return n