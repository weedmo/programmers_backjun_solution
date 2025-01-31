def solution(arr, queries):
    answer = []
    
    for i in queries:
        arr2 = arr[i[0]: i[1] + 1] 
        arr2.sort()  
        
        if len(arr2) == 0 or i[2] >= arr2[-1]:
            answer.append(-1)
        else:
            for j in arr2:
                if i[2] < j:
                    answer.append(j)
                    break
    return answer
