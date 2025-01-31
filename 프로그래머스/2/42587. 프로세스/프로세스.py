
def solution(priorities, location):
    q = priorities
    i, count = 0, 0
    while q[location] != 0:
        if q[i] != 0 and max(q) <= q[i]:
            q[i] = 0
            count += 1
        i = (i+1) % len(priorities)
        
    return count