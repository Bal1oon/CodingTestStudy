# https://school.programmers.co.kr/learn/courses/30/lessons/135807

from math import gcd

def solution(arrayA, arrayB):
    def get_gcd(arr):
        g = arr[0]
        for x in arr[1:]:
            g = gcd(g, x)
        return g
    
    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)
    
    answer = 0

    if all(b % gcdA != 0 for b in arrayB):
        answer = max(answer, gcdA)

    if all(a % gcdB != 0 for a in arrayA):
        answer = max(answer, gcdB)
    
    return answer
