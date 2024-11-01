# https://softeer.ai/practice/6288

import sys

input = sys.stdin.readline
w, n = map(int, input().split())
jewels = []
for _ in range(n):
    weight, price = map(int, input().split())
    jewels.append((weight, price))

jewels.sort(key=lambda x:x[1], reverse=True)

bag = 0
total_p = 0

for weight, price in jewels:
    if weight + bag <= w:
        total_p += price * weight
        bag += weight
    else:
        cut = w - bag
        total_p += price * cut
        break
    
print(total_p)