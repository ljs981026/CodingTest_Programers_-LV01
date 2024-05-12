from collections import Counter
def solution(array):
    array = Counter(array).most_common(2)
    if len(array) == 1:
        return array[0][0]
    if array[0][1] == array[1][1]:
        return -1
    return array[0][0]

print(solution([1, 2, 3, 3, 3, 4]))