def solution(arr1, arr2):
    answer = 0
    if len(arr1) > len(arr2):
        return 1
    if len(arr1) < len(arr2):
        return -1
    if len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0   
        
print(solution([100, 17, 84, 1], [55, 12, 65, 36]))