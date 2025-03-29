# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    if total % 2 == 1:
        return -1
    
    target = total // 2
    n = len(queue1)
    
    arr = queue1 + queue2
    sum1 = sum(queue1)
    
    p1, p2 = 0, n
    count = 0
    
    while count <= n * 3:
        if sum1 == target:
            return count
        
        if p1 >= len(arr) or p2 >= len(arr):
            return -1
        
        if sum1 > target:
            sum1 -= arr[p1]
            p1 += 1
        else:
            sum1 += arr[p2]
            p2 += 1
        count += 1
        
    return -1