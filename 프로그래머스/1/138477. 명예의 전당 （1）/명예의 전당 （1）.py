def solution(k, score):
    result = []
    temple = []
    for n in score:
        temple.append(n)
        temple.sort(reverse = True)
        if len(temple) > k:
            temple.pop()

        result.append(temple[-1])

    return result