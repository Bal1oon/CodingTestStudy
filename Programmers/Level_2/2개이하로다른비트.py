# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    
    for x in numbers:
        if x % 2 == 0:
            answer.append(x+1)
        else:
            b = '0' + bin(x)[2:]
            i = b.rfind('0')
            b = list(b)
            b[i] = '1'
            b[i + 1] = '0'
            answer.append(int(''.join(b), 2))
    return answer