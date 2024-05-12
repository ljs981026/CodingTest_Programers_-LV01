from math import factorial
solution = lambda n : max([i for i in range (1, 11) if factorial(i) <= n]) 

print(solution(7))