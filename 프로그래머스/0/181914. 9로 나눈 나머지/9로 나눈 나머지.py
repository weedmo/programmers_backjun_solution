def solution(number):
    remain = sum([int(i) for i in number]) % 9
    while remain >= 10:
        remain = sum([int(i) for i in str(remain)]) % 9
    return remain