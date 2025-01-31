def solution(rank, attendance):
    for i, b in enumerate(attendance):
        if not b:
            rank[i] = 101
    sorted_rank = sorted(rank)
    return 10000 * rank.index(sorted_rank[0]) + 100 * rank.index(sorted_rank[1]) + rank.index(sorted_rank[2])