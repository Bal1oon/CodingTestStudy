# https://softeer.ai/practice/6280

import sys

n = int(sys.stdin.readline())
answer = 2
for _ in range(n):
    answer = answer * 2 - 1

print(pow(answer, 2))