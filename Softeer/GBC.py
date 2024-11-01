# https://softeer.ai/practice/6270

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

std = [list(map(int, input().split())) for _ in range(n)]
test = [list(map(int, input().split())) for _ in range(m)]

max_over = [0]      # 속도차가 음수만 기록될 수 있어 0 초기설정
while std and test:
    diff_len = test[0][0] - std[0][0]

    if diff_len > 0:
        max_over.append(test[0][1] - std[0][1])
        std.pop(0)
        test[0][0] = diff_len
    elif diff_len < 0:
        max_over.append(test[0][1] - std[0][1])
        std[0][0] = -diff_len
        test.pop(0)
    else:
        max_over.append(test[0][1] - std[0][1])
        std.pop(0)
        test.pop(0)

print(max(max_over))