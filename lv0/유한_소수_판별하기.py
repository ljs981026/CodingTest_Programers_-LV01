import math

def solution(a, b):
    max_div = math.gcd(a,b)
    result = []
    parent = b // max_div
    for i in range(2, parent):
        if parent % i == 0:
            cnt = 0
            for j in range (1, i):
                if i % j == 0:
                    cnt += 1
            if cnt == 1:
                result.append(i) 

    if parent < 3 or parent == 5 or result == [2] or result == [5] or result == [2,5]:
        return 1
    else:
        return 2
    
#유클리드 호제법
def solution(a, b):
    b //= math.gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2

print(solution(7, 20))