# https://www.acmicpc.net/problem/2493

n = int(input())
towers = list(map(int, input().split()))
stack = []

for i in range(n):
    while stack and towers[stack[-1]] < towers[i]:
        stack.pop()
    if stack:
        print(stack[-1] + 1, end = ' ')
    else:
        print(0, end = ' ')
    stack.append(i)