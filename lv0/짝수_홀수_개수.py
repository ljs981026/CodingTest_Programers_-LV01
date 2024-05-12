solution = lambda arr : [list(map(lambda x : 1 if x % 2 == 0 else 0,arr)).count(1), list(map(lambda x : 1 if x % 2 == 0 else 0,arr)).count(0)]

print(solution([1, 3, 5, 7]))