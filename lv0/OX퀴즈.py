def solution(quiz):
    answer = []
    for q in quiz:
        nq = q.split()
        if nq[1] == '-' and (int(nq[0]) - int(nq[2])) == int(nq[4]):
            answer.append("O")
        elif nq[1] == '+' and (int(nq[0]) + int(nq[2])) == int(nq[4]):
            answer.append("O")
        else:
            answer.append("X")            
        
    return answer

    print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))