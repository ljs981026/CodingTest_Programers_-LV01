def solution(names):
    answer = []
    i = 0
    while (i*5) < len(names):
        answer.append(names[i*5:(i*5)+1][0])      
        i += 1
    return answer

def solution(names):
    return names[::5]

print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))