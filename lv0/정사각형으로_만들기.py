def solution(arr):
    max_size = max(len(arr), len(arr[0]))
    answer = [[0] * max_size for i in range(max_size)]    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            answer[i][j] = arr[i][j]
    return answer

print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))