def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i]:
            answer += [arr[i]] *arr[i]*2
        else:
            del answer[-1:-arr[i]-1:-1]
            
    return answer