def solution(s, skip, index):
    answer = ''
    skip_set = set(skip)
    for i in s:
        i_ord = ord(i)
        step = 0
        
        while step < index:
            i_ord += 1
            
            if i_ord > ord('z'):
                i_ord = ord('a')
            if chr(i_ord) not in skip_set:
                step +=1
            
        answer += chr(i_ord)
            
    return answer