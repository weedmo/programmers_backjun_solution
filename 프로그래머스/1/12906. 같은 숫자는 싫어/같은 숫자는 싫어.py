import collections
def solution(arr):
    stack = []
    
    for num in arr:
        stack.append(num)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            
    return stack