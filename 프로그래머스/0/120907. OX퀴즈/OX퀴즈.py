def solution(quiz):
    answer = []
    for i in quiz:
        l, r = i.split('=')
        if eval(l) == int(r):
            answer.append("O")
        else:
            answer.append("X")
    return answer