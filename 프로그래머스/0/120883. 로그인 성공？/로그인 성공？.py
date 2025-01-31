def solution(id_pw, db):
    for ids, pw in db:
        if ids == id_pw[0] and pw == id_pw[1]:
            return 'login'
        elif ids == id_pw[0]:
            return 'wrong pw'
    return 'fail'