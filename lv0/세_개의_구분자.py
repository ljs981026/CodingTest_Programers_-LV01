def solution(myStr):
    abc = ['a','b','c']
    for i in abc:
        if i in myStr:
            myStr = myStr.replace(i, ' ')
        
    if len(myStr.split()) == 0:
        return ["EMPTY"]    
    return myStr.split()

print(solution("baconlettucetomato"))