def solution(t, p):
    t_l = []
    count = 0
    for i in range(0, len(t)-(len(p)-1)):
        t_l.append(t[i:i+len(p)])
        
    for num in t_l:
        if int(p) >= int(num):
            count += 1
    return count