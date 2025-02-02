from collections import Counter
def solution(want, number, discount):
    want_map = dict(zip(want,number))
    count = 0

    for i in range(len(discount)-9):
        want_count = Counter(discount[i:i + 10])
        
        if dict(want_count) == want_map:
            count += 1
    return count