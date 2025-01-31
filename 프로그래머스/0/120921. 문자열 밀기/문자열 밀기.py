def solution(A, B):
    for i in range(len(A)):
        if A == B[i:] + B[:i]:
            return i
    return -1