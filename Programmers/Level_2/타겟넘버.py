# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    stack = [(0, 0)]
    count = 0

    while stack:
        current_sum, index = stack.pop()

        if index == len(numbers):
            if current_sum == target:
                count += 1
            continue

        stack.append((current_sum + numbers[index], index + 1))
        stack.append((current_sum - numbers[index], index + 1))

    return count
