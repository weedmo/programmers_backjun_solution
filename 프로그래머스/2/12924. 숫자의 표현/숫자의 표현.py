def solution(n):
    count = 0
    n2 = n * 2
    for m in range(1, int((n2)**0.5)+1):
        if n2 % m == 0:
            if ((n2//m) - (m-1)) % 2 == 0:
                count += 1
    return count