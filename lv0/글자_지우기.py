my_string = "apporoograpemmemprs"
indices = [1, 16, 6, 15, 0, 10, 11, 3]

def solution(my_string, indices):
    answer = list(my_string)
    indices.sort()
    indices.reverse()
    
    for i in indices:
        answer.pop(i)
        
    return ''.join(answer)

print(solution(my_string, indices))