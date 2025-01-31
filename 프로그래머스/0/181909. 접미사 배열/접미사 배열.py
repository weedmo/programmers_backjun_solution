def solution(my_string):
    answer = []
    string = ''
    for i in my_string[::-1]:
        string += i
        answer.append(string[::-1])
    return sorted(answer)