def solution(arr, flag):
    test = []
    for i in range(len(arr)):
        if flag[i]:
            test.extend([arr[i]] * (arr[i]*2))
        else:
            for i in range(arr[i]):
                test.pop()
    return test

print(solution([3, 2, 4, 1, 3], [True, False, True, False, False]))