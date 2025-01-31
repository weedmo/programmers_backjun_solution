import collections
def solution(strArr):
    change_str = []
    for i in strArr:
        change_str.append(len(i))
        
    count_str = collections.Counter(change_str)
    
    return count_str.most_common()[0][1] 
