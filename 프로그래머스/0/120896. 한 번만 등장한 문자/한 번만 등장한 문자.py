import collections
def solution(s):
    answer = ''
    count_s = collections.Counter(s)
    for key, value in count_s.items():
        if value == 1:
            answer += key
    return ''.join(sorted(answer))