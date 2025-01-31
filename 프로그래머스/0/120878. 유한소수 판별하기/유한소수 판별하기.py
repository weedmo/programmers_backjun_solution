import math
def solution(a, b):
    gcd_b = b // math.gcd(a,b)
    
    while gcd_b % 2 == 0:
        gcd_b //=2
    while gcd_b % 5 == 0:
        gcd_b //= 5
        
    if gcd_b == 1:
        return 1
    return 2