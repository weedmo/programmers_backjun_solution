def solution(s):
    s = [int(i) for i in s.split()]
    result = [str(min(s)), str(max(s))]
    return ' '.join(result)