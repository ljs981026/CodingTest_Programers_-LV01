def solution(hp):
    answer = 0
    ant = [5, 3, 1]
    while hp > 0:
        for i in ant:
            if hp >= i:
                answer += hp // i
                hp %= i
    return answer

print(solution(23))