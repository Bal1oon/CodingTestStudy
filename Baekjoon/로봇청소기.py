# https://www.acmicpc.net/problem/14503

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

count = 0

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        count += 1

    flag = False
    for _ in range(4):
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            r, c = nx, ny
            flag = True
            break

    if not flag:
        back = (d + 2) % 4
        r, c = r + dx[back], c + dy[back]

        if room[r][c] == 1:
            break

print(count)