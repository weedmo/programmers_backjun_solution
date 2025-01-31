def solution(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    composite_count = 0
    for i in range(4, n + 1):
        if not is_prime(i): 
            composite_count += 1

    return composite_count
