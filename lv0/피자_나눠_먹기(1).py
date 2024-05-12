solution = lambda x : 1 if x <= 7 else x // 7 if x % 7 == 0 else x // 7 + 1

print(solution(15))