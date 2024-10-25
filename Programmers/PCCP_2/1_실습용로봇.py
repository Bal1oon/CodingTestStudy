# https://school.programmers.co.kr/learn/courses/15009/lessons/121687

def solution(command):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0), ]    # 상, 우, 하, 좌 방향
    i = 0
    x, y = 0, 0
    
    for c in command:
        if c == 'R':
            i = (i+1) % 4
        elif c == 'L':
            i = (i+3) % 4
        elif c == 'G':
            x, y = x + d[i][0], y + d[i][1]
        elif c == 'B':
            x, y = x - d[i][0], y - d[i][1]

    return [x, y]