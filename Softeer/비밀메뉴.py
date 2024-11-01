# https://softeer.ai/practice/6269

import sys

input = sys.stdin.readline
m, n, k = map(int, input().split())
recipe = ''.join(list(map(str, input().split())))
mani = ''.join(list(map(str, input().split())))

if recipe in mani:
    print('secret')
else:
    print('normal')