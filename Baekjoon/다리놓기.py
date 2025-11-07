# https://www.acmicpc.net/problem/1010

import math

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(math.comb(m, n))
    print(combination(m, n))

# itertools.combinations 를 사용하면 모든 조합을 생성해야 하기 때문에 메모리 초과 또는 시간 초과 발생
# 따라서 math.comb를 사용
# math.comb를 사용하지 못하면 직접 계산
def combination(m, n):
    result = 1
    for i in range(1, n + 1):
        result = result * (m - i + 1) // i
    return result
