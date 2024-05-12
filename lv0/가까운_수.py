def solution(array, n):
    return sorted([[abs(n-i),i] for i in array])[0][1]

print(solution([3, 10, 28],20))