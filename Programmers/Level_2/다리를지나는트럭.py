from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    order, time = 0, 0
    total_weight = 0
    
    while order < len(truck_weights):
        time += 1
        total_weight -= bridge.popleft()
        
        if weight >= total_weight + truck_weights[order]:
            bridge.append(truck_weights[order])
            total_weight += truck_weights[order]
            order += 1
        else:
            bridge.append(0)
            
    time += bridge_length
    
    return time