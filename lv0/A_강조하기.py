def solution(myString):
    answer = ''
    for i in myString:
        if i.isupper():
            if i == 'A':
                answer += i
            else:
                answer += i.lower()
        elif i == 'a':
            answer += i.upper()
        else:
            answer += i
        
    return answer

def solution(myString):
    return myString.lower().replace('a', 'A')

print(solution("abstract algebra"))