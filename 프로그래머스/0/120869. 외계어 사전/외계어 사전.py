def solution(spell, dic):
    spell = sorted(spell)
    for d in dic:
        di = sorted(d)
        if di == spell:
            return 1
    return 2