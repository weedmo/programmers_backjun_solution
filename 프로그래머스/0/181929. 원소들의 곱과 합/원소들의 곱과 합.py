def solution(num_list):
    num1 = pow(sum(num_list), 2)
    num2 = 1
    for i in range(len(num_list)):
        num2 *= num_list[i]
    return int(num1>num2)