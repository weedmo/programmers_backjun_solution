import math
def solution(progresses, speeds):
    stack = []
    answer = []
    
    for p, s in zip(progresses, speeds):
        
        # 총 날짜 계산
        days = math.ceil((100 - p) / s)
            
        if stack and stack[0] < days:
            answer.append(len(stack))
            stack = []
        stack.append(days)
        
    if stack:   
        answer.append(len(stack))
        
    return answer