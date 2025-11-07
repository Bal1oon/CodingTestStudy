# https://www.acmicpc.net/problem/1931

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0

for start, finish in meetings:
    if start >= end:
        count += 1
        end = finish
    
print(count)