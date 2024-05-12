def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)

print(solution(False,True,True,True))