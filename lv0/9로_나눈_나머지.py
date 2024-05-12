def solution(number):
    return sum([int(i) for i in number]) % 9

print(solution("123"))