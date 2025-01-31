def solution(n):
    answer = []
    for i in range(2, int(n)+1):
        if n == 1:
            break
        if n % i == 0:
            answer.append(i)
            while n % i == 0:
                n //= i
    return answer 