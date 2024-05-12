my_string = "ihrhbakrfpndopljhygc"
m = 4
c = 2

def solution(my_string, m, c):
    return ''.join([(my_string[i * m : (i+1) * m])[c-1] for i in range(len(my_string) // m)])

print(solution(my_string, m, c))