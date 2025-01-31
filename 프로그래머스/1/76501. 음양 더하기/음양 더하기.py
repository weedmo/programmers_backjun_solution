def solution(absolutes, signs):
    sum_list = []
    for i in range(len(signs)):
        if signs[i]:
            sum_list.append(absolutes[i])
        else: sum_list.append(-absolutes[i])
    return sum(sum_list) 