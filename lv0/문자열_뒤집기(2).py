my_string = "Progra21Sremm3"
s = 6
e = 12

def solution(my_string, s, e):
    my_string = list(my_string)
    if e == len(my_string):
        return ''.join(my_string[:s] + list(reversed(my_string[s:e+1])))
    return ''.join(my_string[:s] + list(reversed(my_string[s:e+1])) + my_string[e+1:])

print(solution(my_string, s, e))