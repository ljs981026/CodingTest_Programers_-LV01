num1 = 1
num2 = 2

def solution(num1, num2):
    return num1+num2

solution2=lambda *x:sum(x)

print(solution(num1,num2))
print(solution2(num1,num2))