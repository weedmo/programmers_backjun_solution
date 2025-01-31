def solution(n):
    answer = []
    k = [0]*n
    for i in range(n):
        k[i] = 1
        answer.append(k)
        k = [0]*n
    return answer