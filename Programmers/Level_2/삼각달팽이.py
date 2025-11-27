# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    triangle = [[0] * (i + 1) for i in range(n)]
    directions = [(1, 0), (0, 1), (-1, -1)]
    
    max_num = n * (n+1) // 2
    num = 1
    
    x = y = d = 0
    
    while num <= max_num:
        triangle[x][y] = num
        
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= len(triangle[nx]) or triangle[nx][ny] != 0:
            d = (d+1) % 3
            nx = x + directions[d][0]
            ny = y + directions[d][1]
        
        x, y = nx, ny
        num += 1
    
    answer = []
    for i in range(n):
        answer.extend(triangle[i])
    return answer