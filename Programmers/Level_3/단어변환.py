# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def bfs(begin, target, words):
    queue = deque([(begin, 0)])
    visited = set([begin])

    while queue:
        current_word, count = queue.popleft()

        if current_word == target:
            return count

        for word in words:
            if word not in visited:
                diff_count = sum(a != b for a, b in zip(current_word, word))

                if diff_count == 1:
                    visited.add(word)
                    queue.append((word, count + 1))

    return 0

def solution(begin, target, words):
    if target not in words:
        return 0

    answer = bfs(begin, target, words)
    return answer


# ---------------------------------------------------

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    dic_words = dict()
    for word in words:
        dic_words[word] = False
    
    def bfs():
        q = deque([(begin, 0)])
        
        while q:
            cur, cnt = q.popleft()
            if cur == target:
                return cnt
            
            for word in words:
                if not dic_words[word]:
                    diff = sum(a != b for a, b in zip(cur, word))
                    
                    if diff == 1:
                        dic_words[word] = True
                        q.append((word, cnt + 1))
                
    answer = bfs()
    return answer