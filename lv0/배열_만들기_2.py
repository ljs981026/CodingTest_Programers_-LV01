def solution(l, r):
    answer = []
    int_to_str = [str(i) for i in range(l, r+1) if i % 5 == 0]
    for i in int_to_str:
        cnt = 0
        for j in i:
            if j == '0' or j == '5':
                cnt += 1
        if cnt == len(i):
            answer.append(int(i))
    if len(answer)  > 0:
        return answer
    else:
        return [-1]
    

def solution2(l, r):
    answer = []
    for num in range(l, r+1):
        if not set(str(num)) - set(['0','5']):
            answer.append(num)
    return answer if answer else [-1]

print(solution(5,555))
print(solution2(5,555))
