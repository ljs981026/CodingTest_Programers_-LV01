def solution(arr):
    while len(arr) & (len(arr)-1) > 0:
        arr.append(0)
    return arr

print(solution([1, 2, 3, 4, 5, 6]))