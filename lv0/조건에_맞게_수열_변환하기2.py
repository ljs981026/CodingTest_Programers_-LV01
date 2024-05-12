def solution(arr):
    answer = 0
    arr1 = []

    while True:
        for i in arr:
            if i >= 50 and i % 2 == 0:
                arr1.append(i // 2)
            elif i < 50 and i % 2 != 0:
                arr1.append((i*2)+1)
            else:
                arr1.append(i)
        if arr == arr1:
            return answer
        arr = arr1
        arr1 = []
        answer += 1
        
    return answer

print(solution([1, 2, 3, 100, 99, 98]))