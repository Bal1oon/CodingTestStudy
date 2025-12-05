from collections import deque

def hour_to_min(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def min_to_hour(time):
    h, m = divmod(time, 60)
    return f"{h:02d}:{m:02d}"

def solution(n, t, m, timetable):
    table = sorted(hour_to_min(time) for time in timetable)
    bus_table = [540 + t * i for i in range(n)]
    q = deque([x for x in table if x <= bus_table[-1]])

    last_person = -1

    for bus in bus_table:
        cnt = 0

        while q and q[0] <= bus and cnt < m:
            last_person = q.popleft()
            cnt += 1

        # 마지막 버스면 answer 결정
        if bus == bus_table[-1]:
            if cnt < m:  # 만석 아님
                return min_to_hour(bus)
            else:  # 만석임 → last_person보다 1분 먼저 도착
                return min_to_hour(last_person - 1)

# ---------------

from collections import deque

def hour_to_min(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def min_to_hour(time):
    h, m = divmod(time, 60)
    return f"{h:02d}:{m:02d}"

def solution(n, t, m, timetable):
    table = sorted(hour_to_min(time) for time in timetable)
    bus_table = [540 + t * i for i in range(n)]
    q = deque([x for x in table if x <= bus_table[-1]])

    last_person = -1

    for bus in bus_table:
        cnt = 0

        while q and q[0] <= bus and cnt < m:
            last_person = q.popleft()
            cnt += 1

        if bus == bus_table[-1]:
            if cnt < m:
                return min_to_hour(bus)
            else:
                return min_to_hour(last_person - 1)
