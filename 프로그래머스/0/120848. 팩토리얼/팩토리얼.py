def solution(n):
    m = 1
    k = 1
    while n >= m:
        m *= k
        k += 1
    return k-2