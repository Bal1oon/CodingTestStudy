# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    answer = []
    
    def hanoi(n, start, end, mid):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(n-1, start, mid, end)
            answer.append([start, end])
            hanoi(n-1, mid, end, start)
    hanoi(n, 1, 3, 2)
    return answer

print(solution(2))  # [[1, 2], [1, 3], [2, 3]]
print(solution(3))  # [[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]]