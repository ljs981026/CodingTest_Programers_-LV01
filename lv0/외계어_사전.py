def solution(spell, dic):    
    for d in dic:
        cnt = []
        for s in spell:
            if s in d: 
                cnt.append(s)
        if len(set(cnt)) == len(spell):
            return 1
    return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))