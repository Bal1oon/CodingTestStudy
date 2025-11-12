# https://www.acmicpc.net/problem/16953

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
count = 1

while b > a:
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        break
    count += 1

if a == b:
    print(count)
else:
    print(-1)