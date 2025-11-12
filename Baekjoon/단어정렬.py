# https://www.acmicpc.net/problem/1181

n = int(input())
words = []
for _ in range(n):
    w = input()
    if w not in words:
        words.append(w)

words = sorted(words, key=lambda x: (len(x), x))
for w in words:
    print(w)