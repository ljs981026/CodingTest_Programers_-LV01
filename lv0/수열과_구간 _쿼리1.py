def solution(arr, queries):
    for idx, i in enumerate(arr):
        for q in queries:
            if idx >= q[0] and idx <= q[1]:
                arr[idx] += 1
    return arr

print(solution([0, 1, 2, 3, 4], [[0, 1],[1, 2],[2, 3]]))