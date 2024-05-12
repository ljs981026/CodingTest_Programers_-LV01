solution = lambda n, d : [n[-1]]+n[:-1] if d == "right" else n[1:]+[n[0]]

print(solution([1, 2, 3], "right"))