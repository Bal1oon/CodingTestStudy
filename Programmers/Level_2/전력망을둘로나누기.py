# https://school.programmers.co.kr/learn/courses/30/lessons/86971
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(graph, v, visited, x, y):
        visited[v] = True
        cnt = 1
        
        for nx in graph[v]:
            if not visited[nx] and not (v == x and nx == y) and not (v == y and nx == x):
                cnt += dfs(graph, nx, visited, x, y)
        
        return cnt
    
    diff = 101
    for a, b in wires:
        visited = [False] * (n+1)
        cnt = dfs(graph, a, visited, a, b)
        diff = min(diff, abs(n - 2*cnt))
        
    return diff