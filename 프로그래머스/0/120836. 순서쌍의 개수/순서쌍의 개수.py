def solution(n):
    answer = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            answer += 1  # i는 약수
            if i != n // i:
                answer += 1  # (n // i)도 약수로 포함

    return answer
