def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

def solution(numbers):
    result = []
    for n in range(len(numbers)):
        for n2 in range(0, len(numbers)):
            if n == n2:
                continue
            result.append(numbers[n] * numbers[n2])    
    return max(result)

print(solution([1, 2, -3, 4, -5]))