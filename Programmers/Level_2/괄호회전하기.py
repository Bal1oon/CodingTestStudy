# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    for _ in range(len(s)):
        stack = []
        for i in s:
            if i in '[({':
                stack.append(i)
            else:
                if not stack:
                    break
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
        s = s[1:] + s[0]
    return answer

print(solution("[](){}"))	# 3
print(solution("}]()[{"))	#2
print(solution("[)(]"))	# 0
print(solution("}}}"))  # 0