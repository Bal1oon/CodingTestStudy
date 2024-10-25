# https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

def solution(board):
    N = len(board)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    costs = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]  # 방향에 따른 cost 기록
    
    for i in range(4):
        costs[0][0][i] = 0  # 시작점 cost 초기화
    
    def bfs(x, y):
        q = deque()
        
        for i in range(4):
            q.append((x, y, 0, i))  # x, y, cost, direction
        
        while q:
            x, y, cost, direction = q.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                    new_cost = cost + 100
                    
                    if direction != i:  # 방향이 같지 않으면 코너
                        new_cost += 500
                    
                    if new_cost < costs[nx][ny][i]:
                        costs[nx][ny][i] = new_cost
                        q.append((nx, ny, new_cost, i))
                        
    bfs(0, 0)
    return min(costs[N-1][N-1])

# 방향에 따른 cost를 고려하지 않고 2 dimension으로 풀었을 때, 서로 다른 방향에서 온 최소값들을 동시에 저장하지 못하는 문제 발생
## ex) 우로 이동한 700, 아래로 이동한 700. 이후 오른쪽으로 이동할 때 기존 방향을 유지할 수 있기 때문에 800이 되어야 하지만,
## 아래로 이동하는 700이 먼저 실행될 경우 방향이 덮어씌워지기 때문에 1300의 값을 가짐
# 때문에 모든 이동방향으로의 최소값들을 가질 수 있도록 costs를 3D로 설정하였음