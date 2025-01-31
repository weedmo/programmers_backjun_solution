def solution(price):
    if price >= 500000:
        discount_rate = 0.8  # 20% 할인
    elif price >= 300000:
        discount_rate = 0.9  # 10% 할인
    elif price >= 100000:
        discount_rate = 0.95  # 5% 할인
    else:
        discount_rate = 1.0  # 할인 없음

    return int(price * discount_rate)  # 할인 적용 후 정수 반환
