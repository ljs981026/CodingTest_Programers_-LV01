array = [149, 180, 192, 170]
height = 167

def solution(array, height):
    return sum(map(lambda x: 1 if x > height else 0, array))

print(solution(array,height))