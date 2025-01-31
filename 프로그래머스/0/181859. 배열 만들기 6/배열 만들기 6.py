def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if stk == []:
            stk.append(arr[i])
            i+=1
        elif stk != [] and stk[-1] == arr[i]:
            del stk[-1]
            i+=1
        elif stk != [] and stk[-1] != arr[i]:
            stk.append(arr[i])
            i+=1
    if stk == []:
        return [-1]
    else:
        return stk