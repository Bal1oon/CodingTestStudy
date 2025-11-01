from collections import deque

def solution(maze):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maze[nx][ny] == 0:
                    continue
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    q.append((nx, ny))
    
    bfs(0, 0)
    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = [ list(map(int, input())) for _ in range(n) ]

print(solution(maze))