def solution(i, j, k):
    answer = ''
    for i in range(i, j+1):
        for j in str(i):
            answer +=  j
    return answer.count(str(k))