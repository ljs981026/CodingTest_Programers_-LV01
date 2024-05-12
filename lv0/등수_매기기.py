def solution(score):
    avg = [sum(i) for i in score]
    sort_avg = sorted(avg, reverse=True)
    return [sort_avg.index(i) + 1 for i in avg]

print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))