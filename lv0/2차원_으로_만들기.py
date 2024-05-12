def solution(num_list, n):
    answer = []
    a, b = 0, n
    for i in range(1, len(num_list)//n+1):
        answer.append(num_list[a:b])
        a += n
        b += n
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))