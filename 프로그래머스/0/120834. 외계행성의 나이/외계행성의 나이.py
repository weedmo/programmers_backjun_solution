def solution(age):
    answer = ''
    a_ord = ord('a')
    age_list = [int(i) for i in str(age)]
    for i in age_list:
        answer += chr(i+a_ord) 
    return answer