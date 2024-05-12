n = 10
k = 3

def solution(n, k):
    return [i for i in range(1,n+1) if i % k == 0]

def solution2(n, k):
    return [i for i in range(k, n+1, k)]

print(solution(n, k))
print(solution2(n, k))