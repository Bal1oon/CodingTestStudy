# https://softeer.ai/practice/6282

import sys

input = sys.stdin.readline
n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]

def dfs(x, y):
    if not (0 <= x < n and 0 <= y < n) or map[x][y] == 0:
        return 0
    
    map[x][y] = 0
    size = 1
    
    size += dfs(x+1, y)
    size += dfs(x-1, y)
    size += dfs(x, y+1)
    size += dfs(x, y-1)
    
    return size

num = 0
sizes = []
for i in range(n):
    for j in range(n):
        size = dfs(i, j)
        if size > 0:
            num += 1
            sizes.append(size)

sizes.sort()

print(num)
for size in sizes:
    print(size)
