# https://softeer.ai/practice/9498

import sys

input = sys.stdin.readline
s = list(input())
result = []

i=0
while i < len(s):
    if i < len(s) - 1 and s[i] == '(' and s[i+1] == ')':
        result.append('(1')
        i += 1
    elif i < len(s) - 1 and s[i] == ')' and s[i+1] == '(':
        result.append(')+')
        i += 1
    else:
        result.append(s[i])
        i += 1

print(''.join(result))

## 기존 코드 (한개 케이스 시간 초과)
## for문에서의 insert로 인해 시간복잡도 O(kn)

# import sys

# input = sys.stdin.readline
# s = list(input())

# indices = {}
# for i in range(len(s) - 1):
#     if s[i] == '(' and s[i+1] == ')':
#         indices[i] = '1'
#     elif s[i] == ')' and s[i+1] == '(':
#         indices[i] = '+'

# for i in reversed(list(indices.keys())):
#     s.insert(i+1, indices[i])
    
# print(''.join(s))