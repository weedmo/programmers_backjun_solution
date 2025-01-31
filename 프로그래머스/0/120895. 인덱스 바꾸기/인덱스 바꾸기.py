def solution(my_string, num1, num2):
    my_list = [i for i in my_string]
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1]
    return ''.join(my_list)