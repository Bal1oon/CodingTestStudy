# https://school.programmers.co.kr/learn/courses/15009/lessons/121689#

def solution(menu, order, k):
    events = []
    finish_drink = 0
    
    for i in range(len(order)):
        events.append((i * k, 'in'))
        finish_drink = max(finish_drink, i * k) + menu[order[i]]
        events.append((finish_drink, 'out'))
        
    events.sort(key = lambda x: (x[0], x[1] == 'in'))   # out이 먼저 발생되도록 정렬
    max_c, cur_c = 1, 0
    for time, action in events:
        if action == 'in':
            cur_c += 1
        else:
            cur_c -= 1

        max_c = max(max_c, cur_c)
    
    return max_c

# 음료 제조 시간만으로 finish_drink를 설정했을 때, 제조 시간이 짧아 손님의 in 보다 out이 먼저인 경우 발생
# 따라서 '손님이 들어오는 시간'과 '이전 음료 제조 완료 시간'을 비교