solution = lambda n : len([i for i in range(1, n+1) if n % i == 0])

print(solution(20))