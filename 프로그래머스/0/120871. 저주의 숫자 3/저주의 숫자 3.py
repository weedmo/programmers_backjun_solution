def solution(n):
    real_n = 0
    result = 1
    
    while real_n < n:
        
        if '3' not in str(result) and result % 3 != 0:
            real_n += 1
        result += 1
        
    return result -1