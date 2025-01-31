def solution(n):
    plus = 1
    n_1 = bin(n).count('1') 
    n_2 = bin(n+1).count('1')
    while n_1 != n_2:
        plus+=1
        n_2 = bin(n+plus).count('1')
    return n+plus