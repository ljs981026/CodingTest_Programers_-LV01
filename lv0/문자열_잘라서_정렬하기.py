def solution(myString):    
    return sorted((myString.replace('x', ' ')).split())

print(solution("dxccxbbbxaaaa"))