def solution(sides):    
    return 1 if max(sides) < sum(sides) - max(sides) else 2

print(solution([199, 72, 222]))