def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    answer.extend([-1] * (k-len(answer)))

    return answer[:k]

print(solution([0, 1, 1, 2, 2, 3], 3))