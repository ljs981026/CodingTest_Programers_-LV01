import math
solution = lambda n : (abs(6 * n) // math.gcd(6, n)) // 6 

print(solution(10))