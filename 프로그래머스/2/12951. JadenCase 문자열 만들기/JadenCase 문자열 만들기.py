def solution(s):
    result = []
    s_list = s.split(' ')
    for word in s_list:
        
        if word.isalpha():
            word = word[0].upper() + word[1:].lower()
            result.append(word)
        else:
            word = word.lower()
            result.append(word)
    return ' '.join(result)