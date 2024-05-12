my_string = "Programmers"

def solution(my_string):
    answer = [0] * 52
    for i in my_string:
        if i.isupper():
            k = 65
        else:
            k = 71
        answer[ord(i) - k] += 1
    return answer

print(solution(my_string))