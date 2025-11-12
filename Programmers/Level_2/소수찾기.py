# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
import math

def solution(numbers):
    answer = 0
    
    nums = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            nums.add(int(''.join(p)))
    
    for i in list(nums):
        if is_prime(i):
            answer += 1

    return answer

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True