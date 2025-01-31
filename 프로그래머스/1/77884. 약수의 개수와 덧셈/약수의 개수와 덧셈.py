def solution(left, right):
    lr_list = []
    for i in range(left, right+1):
        
        if int(i ** 0.5) ** 2 == i: 
            lr_list.append(-i)
        else:
            lr_list.append(i)
    return sum(lr_list)