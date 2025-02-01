def solution(s):
    answer = []
    hash_map = {}
    
    for i, strs in enumerate(s):
        if strs not in hash_map:
            hash_map[strs] = i
            answer.append(-1)
        else:
            answer.append(i - hash_map[strs])
            hash_map[strs] = i
    return answer