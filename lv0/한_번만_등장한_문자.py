solution = lambda x : ''.join(sorted([i for i in x if x.count(i) == 1]))

print(solution("abdc", "abcd"))