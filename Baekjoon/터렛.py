def solution(x1, y1, r1, x2, y2, r2):
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if d == 0 and r1 == r2:
        return -1
    elif d == 0 and r1 != r2:
        return 0
    elif d > r1 + r2 or d < abs(r1 - r2):
        return 0
    elif d == r1 + r2 or d == abs(r1 - r2):
        return 1
    else:
        return 2

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(solution(x1, y1, r1, x2, y2, r2))
