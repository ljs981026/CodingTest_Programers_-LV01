def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]

def solution(my_str, n):
    answer = []
    cnt = 0
    if len(my_str) % n == 0:
        nls = len(my_str) // n
    else:
        nls = len(my_str) // n + 1
    
    for nl in range(nls):
        answer.append(my_str[cnt:cnt+n])
        cnt += n
        
    return answer

print(solution("abc1Addfggg4556b"))