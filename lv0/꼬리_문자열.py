solution = lambda sl, ex : ''.join([i for i in sl if ex not in i])

print(solution(["abc", "def", "ghi"], "ef"))