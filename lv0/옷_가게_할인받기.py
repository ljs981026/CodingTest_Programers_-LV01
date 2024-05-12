solution = lambda x : int(x * 0.8) if x // 10000 >= 50 else int(x * 0.9) if x // 10000 >= 30 else int(x * 0.95) if x // 10000 >= 10 else x

print(solution(580000))