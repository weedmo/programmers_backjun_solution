def solution(myString):
    answer = ''
    for i in myString:
        if i not in 'abcdefghijk':
            answer += i
        else:
            answer += 'l'
    return answer