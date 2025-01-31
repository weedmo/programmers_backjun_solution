import collections

def solution(participant, completion):
    freqs = collections.Counter(participant)
    
    for name in completion:
        if name in freqs:
            freqs[name] -= 1
            
    return freqs.most_common(1)[0][0]