# https://softeer.ai/practice/9657

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

destroyers = []
for _ in range(n):
    destroyers.append(list(map(int, input().split())).count(1))
attacks = [list(map(int, input().split())) for _ in range(2)]

for l, r in attacks:
    for i in range(l-1, r):
        destroyers[i] -= 1 if destroyers[i] > 0 else 0
        
result = sum(destroyers[i] for i in range(n))
print(result)