def solution(arr):
    a = 1
    while a < len(arr):
        a *= 2
    if a == len(arr):
        return arr
    else: 
        return arr+[0]*(a-len(arr))
    return answer