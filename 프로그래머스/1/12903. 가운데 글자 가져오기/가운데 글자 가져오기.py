def solution(s):
    if len(s) == 1:
        return s
    elif len(s) % 2 == 0:
        return s[len(s)//2-1: len(s)//2+1]
    else:
        return s[len(s)//2]