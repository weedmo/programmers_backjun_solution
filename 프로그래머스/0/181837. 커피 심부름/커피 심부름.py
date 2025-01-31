def solution(order):
    total = 0
    for i in order:
        if 'americano' in i or i == "anything":
            total += 4500
        else:
            total += 5000
    return total