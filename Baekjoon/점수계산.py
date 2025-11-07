# https://www.acmicpc.net/problem/2822

scores = []
for i in range(8):
    score = int(input())
    scores.append((score, i + 1))

scores.sort(reverse=True)
top_scores = scores[:5]
print(sum(score[0] for score in top_scores))
top_scores.sort(key=lambda x: x[1])
print(*[score[1] for score in top_scores])
