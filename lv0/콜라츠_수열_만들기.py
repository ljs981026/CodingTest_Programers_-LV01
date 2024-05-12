def solution(n):
    answer = []
    while True:
        answer.append(int(n))
        if n == 1:
            break
        else:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
    return answer

print(solution(10))