def solution(myString, pat):
    right = len(myString)
    
    while myString[right - len(pat):right] != pat:
        right -= 1
    return myString[:right]