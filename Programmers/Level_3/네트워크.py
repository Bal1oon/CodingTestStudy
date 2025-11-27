# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution_dfs(n, computers):
    visited = [False] * n
    answer = 0
    
    def dfs(v):
        visited[v] = True
        
        for i in range(n):
            if not visited[i] and computers[v][i] == 1:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer

# ---------------------------------------------------

from collections import deque

def solution_bfs(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            q = deque([i])
            visited[i] = True

            while q:
                v = q.popleft()
                for j in range(n):
                    if not visited[j] and computers[v][j] == 1:
                        visited[j] = True
                        q.append(j)
    return answer