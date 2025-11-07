w, h = map(int, input().split())
n = int(input())

vertical = [0, h]
horizontal = [0, w]

for _ in range(n):
    direction, num = map(int, input().split())
    if direction == 0:
        vertical.append(num)
    else:
        horizontal.append(num)

vertical.sort()
horizontal.sort()

max_vertical = max(vertical[i+1] - vertical[i] for i in range(len(vertical) -1))
max_horizontal = max(horizontal[i+1] - horizontal[i] for i in range(len(horizontal) -1))

print(max_vertical * max_horizontal)
