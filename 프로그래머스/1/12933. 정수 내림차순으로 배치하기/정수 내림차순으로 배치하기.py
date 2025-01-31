def solution(n):
    list_n = [i for i in str(n)]
    return int(''.join(sorted(list_n, reverse=True)))