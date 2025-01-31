def solution(s):
    stack = []
    
    for p in s:
        if not stack and p ==')':
            return False
        if p == '(':
            stack.append(p)
        elif stack and p == ')':
            stack.pop()

    return len(stack) == 0