def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

def solution(my_string):
    answer = []
    type = ''
    for m in my_string.split():
        if m.isdigit():
            if type == '-':
                m = '-' + m 
            answer.append(int(m))
        else:
            if m == '-':
                type = '-'
            else:
                type = '+'
        
    return sum(answer)

print(solution("3 + 4"))