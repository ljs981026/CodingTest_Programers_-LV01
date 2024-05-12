def solution(intStrs, k, s, l):    
    return [int(i[s:s+l]) for i in intStrs if int(i[s:s+l]) > k]

print(solution(["0123456789","9876543210","9999999999999"], 50000, 5, 5))