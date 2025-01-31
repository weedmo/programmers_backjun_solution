def solution(score):
    sum_scores = [sum(i) for i in score]
    sorted_scores = sorted(sum_scores, reverse = True)
    
    rank_scores = [sorted_scores.index(i) +1 for i in sum_scores]
    return rank_scores