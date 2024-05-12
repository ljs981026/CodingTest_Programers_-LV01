num1 = 10
num2 = 5

solution = lambda num1, num2 : num1 // num2
solution2 = int.__floordiv__

print(solution(num1,num2))
print(solution2(num1,num2))