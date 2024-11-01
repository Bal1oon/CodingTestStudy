# https://softeer.ai/practice/7374

import sys

input = sys.stdin.readline
grid = [list(map(int, input().split())) for _ in range(3)]

min_cost = float('inf')
for target in range(1, 4):
    for i in range(3):
        a, b, c = grid[i][0],  grid[i][1],  grid[i][2]
        cost = abs(target-a) + abs(target-b) + abs(target-c)
        min_cost = min(min_cost, cost)
    for i in range(3):
        a, b, c = grid[0][i],  grid[1][i],  grid[2][i]
        cost = abs(target-a) + abs(target-b) + abs(target-c)
        min_cost = min(min_cost, cost)

print(min_cost)