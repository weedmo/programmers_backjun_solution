def solution(s):
    s = s.split(' ')
    s_ = ''
    s_list = []
    for i in s:
        for j in range(len(i)):
            if j == 0:
                s_ += i[j].upper()
            elif j % 2 == 0:
                s_ += i[j].upper()
            else:
                s_ += i[j].lower()
                
        s_list.append(s_)
        s_ = '' 
        
    return ' '.join(s_list)