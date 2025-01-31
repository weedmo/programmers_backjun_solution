def solution(l, r):
    result = []
    for num in range(l, r + 1):
        num_str = str(num)
        if all(i in ('0', '5') for i in num_str):
            result.append(int(num_str))
    return result if result else [-1]