def solution(numbers):
    answer = 0
    result = sorted(numbers, key = lambda x : x)[-2:]
    return result[0] * result[1]


print(solution([0, 31, 24, 10, 1, 9]))