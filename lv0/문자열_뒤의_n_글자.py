def solution(my_string, n):
    return my_string[len(my_string)-n:]

def solution2(my_string, n):
    return my_string[-n:]

print(solution("ProgrammerS123", 11))
print(solution2("He110W0r1d", 5))