def solution(myString, pat):
    change_str = myString.replace('A', 'b').replace('B', 'a').upper()
    return int(bool(pat in change_str))