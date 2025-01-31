from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length) 
    truck_weights = deque(truck_weights)  
    count = 0 
    current_weight = 0  
    
    while bridge:
        count += 1
        # out
        out = bridge.popleft()  
        current_weight -= out 
        
        if truck_weights:
            # income
            if current_weight + truck_weights[0] <= weight:
                incom = truck_weights.popleft()
                bridge.append(incom)
                current_weight += incom
            else:
                bridge.append(0)  
    
    return count
