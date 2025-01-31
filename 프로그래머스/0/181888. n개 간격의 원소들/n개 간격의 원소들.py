def solution(num_list, n):
    answer = []
    i = 0
    while len(num_list) > i:
        answer.append(num_list[i])
        i += n
    return answer