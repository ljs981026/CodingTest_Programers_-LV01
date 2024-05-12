solution = lambda nl, n : [-i[1] for i in sorted(list(map(lambda x : [abs(x-n), -x], nl)), key = lambda x : (x[0], x[1]))]

def solution(numlist, n):
    return sorted(numlist,key = lambda x: [abs(x-n),-x])

print(solution([10000,20,36,47,40,6,10,7000], 30))