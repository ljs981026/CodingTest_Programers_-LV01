def solution(sides):
    answer = 0

    # 첫번째 경우
    for i in range (1, sum(sides)+1):
        if i < sum(sides) and i > max(sides):
            answer += 1
    # 두번째 경우
    for i in range (1, max(sides)+1):
        if max(sides) < i + min(sides):
            answer += 1
            
    return answer

print(solution([3, 6]))