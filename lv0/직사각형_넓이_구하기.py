def solution(dots):
    width = [i[0] for i in dots]
    height = [i[1] for i in dots]
    width = max(width) - min(width)
    height = max(height) - min(height)
    return width * height

solution = lambda d : (max(d)[0] - min(d)[0]) * (max(d)[1] - min(d)[1])

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))