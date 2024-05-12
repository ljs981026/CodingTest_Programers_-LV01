def solution(cipher, code):
    return ''.join(list(map(lambda x : cipher[x-1], [code*i for i in range(1,(len(cipher) // code) + 1)])))

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer

print(solution("dfjardstddetckdaccccdegk", 4))