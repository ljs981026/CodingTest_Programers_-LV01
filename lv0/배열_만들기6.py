def solution(arr):
    stk = []
    i = 0
    while i < len(arr):   
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] == arr[i]:
                stk.pop()
                i += 1
            else:
                stk.append(arr[i])
                i += 1
    if len(stk) == 0:
        return [-1]
    else:
        return stk
    
print(solution([0, 1, 1, 1, 0]))