# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    tickets.sort()
    result = []
    visited = [False] * len(tickets)
    
    def dfs(cur, path, visited):
        if len(path) == len(tickets) + 1:
            result.append(path)
            return
        
        for i in range(len(tickets)):
            if not visited[i] and cur == tickets[i][0]:
                visited[i] = True
                dfs(tickets[i][1], path + [tickets[i][1]], visited)
                visited[i] = False
        
    dfs('ICN', ['ICN'], visited)
    return result[0]

# ---
# def solution(tickets):
#     tickets.sort()
#     visited = [False] * len(tickets)
#     answer = []
    
#     def dfs(path, used):
#         if used == len(tickets):
#             answer.append(path)  
#             return
        
#         for i, (start, end) in enumerate(tickets):
#             if not visited[i] and start == path[-1]:
#                 visited[i] = True
#                 dfs(path + [end], used + 1)
#                 visited[i] = False
        
#     dfs(['ICN'], 0)
    
#     return answer[0]