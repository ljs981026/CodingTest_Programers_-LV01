array = [1,1,2,3,5]
n = 1
def solution(array, n):
    return sum(list(map(lambda x : 1 if x == n else 0, array)))

def solution2(array, n):
    return array.count(n)

print(solution(array,n))
print(solution2(array,n))