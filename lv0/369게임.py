def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

solution = lambda o : len([i for i in str(o) if i == '3' or i == '6' or i == '9'])

print(solution(29423))