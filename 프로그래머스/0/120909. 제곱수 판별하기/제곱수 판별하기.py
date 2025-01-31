def solution(n):
    k = 1
    while k**2 <= n:
        if k**2 ==n:
            return 1
        k += 1
        
    return 2