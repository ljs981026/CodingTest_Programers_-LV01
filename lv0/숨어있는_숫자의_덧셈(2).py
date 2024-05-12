def solution(my_string):
    answer = 0  
    result = '0'
    for idx,m in enumerate(my_string):
        if m.isdigit():
            result += m
            if idx == len(my_string)-1:
                answer += int(result)
        else:            
            answer += int(result)
            result = '0'
    return answer

solution = lambda x : sum(int(i) for i in ''.join(i if i.isdigit() else ' ' for i in x).split())

print(solution("aAb1B2cC34oOp"))