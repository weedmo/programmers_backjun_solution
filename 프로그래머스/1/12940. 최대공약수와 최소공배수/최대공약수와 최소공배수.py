import math
def solution(n, m):
    nm_gcd = math.gcd(n,m)
    
    return [nm_gcd, nm_gcd * n//nm_gcd * m//nm_gcd]