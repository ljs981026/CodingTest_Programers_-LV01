q = 3
r = 1
code = "qjnwezgrpirldywt"

def solution(q, r, code):
    return "".join([list(code)[i] for i in range(len(list(code))) if i % q == r])

print(solution(q,r,code))