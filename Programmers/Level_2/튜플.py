# https://school.programmers.co.kr/learn/courses/30/lessons/64065

# list와 이중for문 사용 -> len(answer)가 커질수록 느려짐
def solution(s):
    s = s[2:-2].split('},{')
    s = sorted(s, key = lambda x : len(x))
    
    answer = []
    for i in s:
        m = list(map(int, i.split(',')))
        n = [item for item in m if item not in answer]
        answer.append(n[0])
    return answer

# set 자료형을 통한 차집합으로 위 방법보다 효율적
def solution2(s):
    answer = []
    
    sets = s[2:-2].split("},{")
    sets = sorted(sets, key = lambda x : len(x))
    
    for i in sets:
        m = set(map(int, i.split(",")))
        n = m - set(answer)
        answer.append(list(n)[0])
        
    return answer

# solution2는 list와 set 자료형을 자주 변환하다보니 set을 추가로 하나 두는 게 더 나은 방향임
def solution3(s):
    answer = []
    answer_set = set()

    sets = s[2:-2].split("},{")
    sets = sorted(sets, key = lambda x : len(x))

    for i in sets:
        m = set(map(int, i.split(",")))
        n = m - answer_set
        val = list(n)[0]
        answer.append(val)
        answer_set.add(val)
    
    return answer