def solution(arr):
    answer = 0
    test1 = []
    test2 = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            test1.append(arr[i][j])
            test2.append(arr[j][i])
    return 1 if test1 == test2 else 0
    
print(solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]))