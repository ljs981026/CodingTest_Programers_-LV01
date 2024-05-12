def solution(todo_list, finished):
    answer = []
    for i in dict(zip(todo_list, finished)):
        if dict(zip(todo_list,finished))[i] == False: 
            answer.append(i)
        
    return answer

print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"],	[True, False, True, False]))