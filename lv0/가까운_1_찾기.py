arr = [1,1,1,1,0]
idx = 3

def solution(arr, idx):
    answer = arr[idx:]
    for i in range(len(answer)):
        if answer[i] == 1:
            return idx + i
    return -1

print(solution(arr, idx))