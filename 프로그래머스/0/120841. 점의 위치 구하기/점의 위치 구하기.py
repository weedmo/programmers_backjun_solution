def solution(dot):
    i, j = dot  # 단일 좌표 분해
    if i > 0 and j > 0:
        return 1  # 제1 사분면
    elif i < 0 and j > 0:
        return 2  # 제2 사분면
    elif i < 0 and j < 0:
        return 3  # 제3 사분면
    elif i > 0 and j < 0:
        return 4  # 제4 사분면
    else:
        return 0  # 원점 또는 경계
