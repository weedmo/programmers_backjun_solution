def solution(angle):
    answer = 0
    if angle > 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle == 180:
        answer = 4
    else:
        answer = 3
    return answer