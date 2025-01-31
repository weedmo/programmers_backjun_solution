def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    for i, p in enumerate(prices):
        while stack and p < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
        
    if stack:
        for i in stack:
            answer[i] = len(prices) -1 -i
            
    return answer