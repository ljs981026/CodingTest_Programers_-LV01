def solution(chicken):
    answer = 0
    while chicken >= 10:
        eat = chicken // 10
        chicken = eat + chicken % 10
        answer += eat

    return answer

print(solution(1081))

