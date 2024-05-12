def solution(id_pw, db):    
    for i in db:
        if i[0] == id_pw[0]:
            # 비밀번호 일치하는지 판단
            if i[1] == id_pw[1]:
                return 'login'
            else:
                return 'wrong pw'            
    return 'fail'

print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))