def solution(rank, attendance):
    test = sorted(([[i, idx] for idx, i in enumerate(rank) if attendance[idx] == 1]))[:3] 
    return 10000 * test[0][1] + 100 * test[1][1] + test[2][1]

print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))