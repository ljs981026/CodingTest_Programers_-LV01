def solution(num_list):
    answer = 1
    for i in num_list:
        answer *= i
    return sum(num_list) if len(num_list) >= 11 else answer

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))