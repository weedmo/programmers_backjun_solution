def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma" ]
    for i in babbling:
        for j in baby:
            i = i.replace(j, " ")
        if i.strip() == "":
            answer += 1
    
    return answer