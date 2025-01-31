import collections
def solution(clothes):
    clothes = [c[1] for c in clothes]
    freqs = collections.Counter(clothes)
    result = 1
    
    for i in freqs.values():
        result *= i + 1
    return result -1