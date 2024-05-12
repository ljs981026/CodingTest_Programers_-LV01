def solution(my_string, num1, num2):
    answer = ''
    for idx,i in enumerate(my_string):
        if idx == num1:
            answer += my_string[num2]
        elif idx == num2:
            answer += my_string[num1]
        else:
            answer += i
    
    return answer

print(solution("I love you", 3,	6))