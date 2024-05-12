def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))

print(solution([4, 2, 6, 1, 7, 6]))