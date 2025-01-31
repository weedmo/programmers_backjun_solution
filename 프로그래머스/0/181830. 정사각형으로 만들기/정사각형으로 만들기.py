def solution(arr):
    max_len = max(len(arr), len(max(arr, key=lambda x: len(x))))
    answer = [[0]*max_len for _ in range(max_len)]
    
    for i, a in enumerate(arr):
        for j in range(len(a)):
            answer[i][j] = a[j]
        
    return answer