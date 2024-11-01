# https://softeer.ai/practice/7628

import sys

n = int(input())
r_list = list(map(int, input().split()))

answer = 0
for i in range(2, 101):
    count = sum(1 for r in r_list if r % i == 0)
    answer = max(answer, count)

print(answer)