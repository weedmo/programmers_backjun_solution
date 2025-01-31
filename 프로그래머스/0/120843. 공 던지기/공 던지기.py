def solution(numbers, k):
    answer = []
    for i in range(k):
        if i*2 >= len(numbers):
            i = (i*2) % len(numbers)
            answer.append(numbers[i])
        else:
            answer.append(numbers[i*2])

    return answer[-1]