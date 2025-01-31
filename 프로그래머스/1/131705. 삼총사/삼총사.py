from itertools import combinations

def solution(number):
    count = sum(1 for comb in combinations(number, 3) if sum(comb) == 0)
    return count
