def solution(myString, pat):
    for i in range(len(myString)):
        if i == 0 and myString[0:].endswith(pat):
            return myString
        if myString[:-i].endswith(pat):
            return myString[:-i]
        
print(solution("AbCdEFG", "dE"))