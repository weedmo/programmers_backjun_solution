def solution(n):
    b = 6
    r = n % b
    while  r != 0:
        b, r = r, b % r
        
    return n / b