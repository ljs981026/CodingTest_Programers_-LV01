def solution(myString, pat):
    return 1 if pat in ''.join(map(lambda x : 'B' if x == 'A' else 'A', myString)) else 0

print(solution("ABBAA", "AABB"))