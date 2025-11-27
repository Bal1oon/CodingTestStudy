# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)
                
    def bfs(start, end):
        visited = [[False] * n for _ in range(m)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        q = deque()
        q.append((*start, 0))
        visited[start[0]][start[1]] = True
        
        while q:
            x, y, t = q.popleft()
            
            if (x, y) == end:
                return t
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        q.append((nx, ny, t + 1))
                        
        return -1
                
    d1 = bfs(S, L)
    if d1 == -1:
        return -1
    
    d2 = bfs(L, E)
    if d2 == -1:
        return -1

    return d1 + d2