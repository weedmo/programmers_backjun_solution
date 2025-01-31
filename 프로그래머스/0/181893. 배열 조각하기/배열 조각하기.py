def solution(arr, query):
    for i, n in enumerate(query):
        if i % 2 == 0:
            del arr[n+1:]
        else:
            del arr[:n]
    return arr