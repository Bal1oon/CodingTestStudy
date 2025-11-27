# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    MOD = 1000000007
    
    d = [[0] * m for _ in range(n)]
    puddles = {(j-1, i-1) for i, j in puddles}

    d[0][0] = 1
    for i in range(n):
        for j in range(m):
            if (i, j) in puddles:
                d[i][j] = 0
            else:
                if i > 0:
                    d[i][j] += d[i-1][j]
                if j > 0:    
                    d[i][j] += d[i][j-1]
    
    return d[n-1][m-1] % MOD