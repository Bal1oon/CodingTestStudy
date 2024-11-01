# https://softeer.ai/practice/6266

import sys
from collections import defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())

meetings = defaultdict(list)

rooms = [input().rstrip() for _ in range(n)]
rooms.sort()

for _ in range(m):
    r, s, t = input().split()
    meetings[r].append((int(s), int(t)))

meet_available = defaultdict(list)
for r in rooms:
    meetings[r].sort()
    
    start, end = 9, 18

    if meetings[r]:
        for meet_start, meet_end in meetings[r]:
            if start < meet_start:
                meet_available[r].append((start, meet_start))
            start = meet_end
            
        if start < end:
            meet_available[r].append((start, end))
    else:
        meet_available[r].append((start, end))

for i in range(n):
    room = rooms[i]
    print(f'Room {room}:')
    if not meet_available[room]:
        print('Not available')
    else:
        print(f'{len(meet_available[room])} available:')
        for meet in meet_available[room]:
            print(f'{meet[0]:02}-{meet[1]:02}')

    if i < n-1:
        print('-----')
