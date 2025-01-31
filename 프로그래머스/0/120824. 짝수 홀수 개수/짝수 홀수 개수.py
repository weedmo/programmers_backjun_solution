def solution(num_list):
    num1 = 0
    for i in num_list:
        if i % 2 == 0:
            num1 += 1
    return [num1, len(num_list)-num1]