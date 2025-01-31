def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append([num_list[j] for j in range(i, i+n)])
    return answer