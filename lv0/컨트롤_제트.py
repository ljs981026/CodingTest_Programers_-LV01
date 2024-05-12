def solution(s):
    answer = 0
    for idx,i in enumerate(s.split()):
        try: answer += int(i)
        except: answer -= int(s.split()[idx-1])
    return answer

print(solution("1 2 Z 3"))