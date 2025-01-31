def solution(x):
    sum_x = sum([int(i) for i in str(x)])
    return bool(x % sum_x == 0)