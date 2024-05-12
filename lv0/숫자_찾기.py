def solution(num, k):
    num = list(str(num))
    if num.count(str(k)) > 0:
        return num.index(str(k))+1
    else:
        return -1
    
print(solution(29183, 1))