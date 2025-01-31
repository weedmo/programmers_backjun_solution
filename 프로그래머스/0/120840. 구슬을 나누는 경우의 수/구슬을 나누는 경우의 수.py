def solution(balls, share):
    def fac(a):
        k = 1
        for i in range(1,a+1):
            k*=i
        return k
    return fac(balls)/(fac(balls-share) * fac(share))