def solution(arr):
    two_list = []
    for i in range(len(arr)):
        if arr[i] == 2:
            two_list.append(i)
    try:
        return arr[two_list[0]:two_list[-1]+1]        
    except:
        return [-1]

print(solution([1, 2, 1, 4, 5, 2, 9]))