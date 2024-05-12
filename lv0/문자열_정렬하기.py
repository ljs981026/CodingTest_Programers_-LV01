import re

def solution(my_string):
    answer = []
    for i in my_string:
        if i in [str(i) for i in range(0,10)]:
            answer.append(int(i))
    answer.sort() 
    return answer

def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))

solution = lambda ms : sorted([int(i) for i in ms if i.isdigit()])

print(solution("p2o4i8gj2"))