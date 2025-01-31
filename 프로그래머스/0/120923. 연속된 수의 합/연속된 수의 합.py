def solution(num, total):
    answer = []
    if total % num == 0:
        return [i for i in range(total//num - num//2,total//num - num//2 + num)]
    else:
        return [i for i in range(total//num - num//2+1, total//num - num//2 + 1 + num)]