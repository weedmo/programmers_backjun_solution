def solution(dots):
    dots = sorted(dots)
    return abs((dots[0][0] - dots[2][0]) * (dots[0][1] - dots[1][1]) )