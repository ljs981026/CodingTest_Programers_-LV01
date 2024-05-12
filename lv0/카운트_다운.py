start = 10
end_num = 3

def solution(start, end_num):
    return list(reversed([i for i in range(end_num, start+1)]))

def solution2(start, end_num):
    return list(range(start, end_num-1, -1))

print(solution(start, end_num))
print(solution2(start, end_num))