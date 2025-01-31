def solution(arr):
    range_arr = []
    if 2 not in arr:
        return [-1]
    
    for i in range(len(arr)):
        if arr[i] == 2:
            range_arr.append(i)
            
    if len(range_arr) >= 2:
        return arr[range_arr[0]:range_arr[-1]+1]
    else:
        return [2]