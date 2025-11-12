# https://www.acmicpc.net/problem/1015

n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a)
answer = [0] * n

for i in range(n):
    idx = sorted_a.index(a[i])
    answer[i] = idx
    sorted_a[idx] = -1

print(*answer)