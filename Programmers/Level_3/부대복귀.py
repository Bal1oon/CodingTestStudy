from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    queue = deque([destination])
    dist = [-1] * (n+1)
    dist[destination] = 0
    
    while queue:
        cur = queue.popleft()
        for neighbor in graph[cur]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[cur] + 1
                queue.append(neighbor)
                
    answer = []
    for source in sources:
        answer.append(dist[source])
        
    return answer