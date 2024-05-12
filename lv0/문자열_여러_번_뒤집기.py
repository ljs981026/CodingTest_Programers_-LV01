def solution(my_string, queries):
    for i in queries:
        my_string = my_string[:i[0]] + my_string[i[0]:i[1]+1][::-1] + my_string[i[1]+1:]
    return my_string

print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))