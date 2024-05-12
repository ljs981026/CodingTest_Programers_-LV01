import re
def solution(my_string):
    return sum(map(int, (list(re.sub('^[0-9]', '', my_string)))))

solution = lambda ms : sum([int(i) for i in ms if i.isdigit()])

print(solution("aAb1B2cC34oOp"))