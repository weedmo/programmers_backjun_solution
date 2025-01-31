def solution(n, words):
    answer = []
    
    for i, word in enumerate(words):
        if not answer:
            answer.append(word)
            continue
        if word not in answer and word[0] == words[i-1][-1] :
            answer.append(word)
        else:
            return [i % n + 1, i // n + 1]
    return [0,0]
