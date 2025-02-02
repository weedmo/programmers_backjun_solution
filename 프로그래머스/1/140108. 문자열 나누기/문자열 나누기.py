def solution(s):
    x, not_x, count = 0, 0, 0
    main_word = []
    
    for word in s:
        if main_word == []:
            main_word.append(word)
            x += 1
        else:
            if main_word and word == main_word[0]:
                x += 1
            else:
                not_x += 1
        
        if x == not_x:
            main_word.pop()
            count += 1
            x, not_x = 0, 0
            
    if main_word:
        count += 1
    return count