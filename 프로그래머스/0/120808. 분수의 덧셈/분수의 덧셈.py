from math import gcd

def solution(numer1, denom1, numer2, denom2):
    lcm = (denom1 * denom2) // gcd(denom1, denom2)
    
    new_numer = (numer1 * (lcm // denom1)) + (numer2 * (lcm // denom2))
    new_denom = lcm

    greatest_common_divisor = gcd(new_numer, new_denom)
    new_numer //= greatest_common_divisor
    new_denom //= greatest_common_divisor

    return [new_numer, new_denom]
