def solution(strArr):
    answer = []
    temp = 1
    for i in strArr:
        if temp == 1:
            answer.append(i.lower())
            temp +=1
        else:
            answer.append(i.upper())
            temp -= 1
    return answer