# https://softeer.ai/practice/7703

import sys

input = sys.stdin.readline
n = int(input())

puzzle = []
for _ in range(n):
    s, t = input().upper().split()
    puzzle.append(t[s.index('X')])

print(''.join(puzzle))