def solution(arr, n):
    length = len(arr)
    if length % 2 == 0:
        return [(arr[i]+n) if i % 2 != 0 else arr[i] for i in range(length)]
    else:
        return [(arr[i]+n) if i % 2 == 0 else arr[i] for i in range(length)]
    
print(solution([49, 12, 100, 276, 33], 27))