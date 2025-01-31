def solution(chicken):
    tortal = 0
    
    while chicken >= 10:
        tortal += chicken // 10
        surplus = chicken % 10 + chicken // 10
        chicken = surplus
    return tortal