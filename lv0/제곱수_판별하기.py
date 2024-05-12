from math import sqrt

solution = lambda n : 1 if int(sqrt(n))**2 == n else 2 

def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

print(solution(976))