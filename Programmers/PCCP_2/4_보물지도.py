# https://school.programmers.co.kr/learn/courses/15009/lessons/121690

from collections import deque

def solution(n, m, hole):
    grid = [[0] * (n+1) for _ in range(m+1)]
    for x, y in hole:
        grid[y][x] = -1 # 함정
    
    q = deque()
    q.append((1, 1, 0, False))  # x, y, 시간, 신발 사용
    visited = set()
    visited.add((1, 1, False))  # x, y, 신발 사용
    
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    while q:
        x, y, time, use_shoe = q.popleft()
        
        if x == n and y == m:
            return time
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 1 <= nx <= n and 1 <= ny <= m and grid[ny][nx] != -1 and (nx, ny, use_shoe) not in visited:
                q.append((nx, ny, time + 1, use_shoe))
                visited.add((nx, ny, use_shoe))
            
        if not use_shoe:
            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 1 <= nx <= n and 1 <= ny <= m and grid[ny][nx] != -1 and (nx, ny) not in visited:
                    q.append((nx, ny, time + 1, True))
                    visited.add((nx, ny, True))
        
    return -1