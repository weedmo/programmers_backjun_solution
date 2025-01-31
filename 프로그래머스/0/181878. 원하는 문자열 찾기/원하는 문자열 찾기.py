def solution(myString, pat):
    return int(bool(pat.lower() in myString.lower()))