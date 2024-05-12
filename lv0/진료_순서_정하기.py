solution = lambda e : [item for item2 in [[idx2+1 for idx2,j in enumerate(sorted(e, key = lambda x : x,reverse=True)) if i == j]for idx1,i in enumerate(e)] for item in item2]

print(solution([3, 76, 24]))