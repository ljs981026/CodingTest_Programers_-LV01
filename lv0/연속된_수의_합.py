def solution(num, total):
    answer = [] 
    cnt = 0
    if total == 0:
        for i in range(1,(num+1) // 2):
            answer.append(-i)
            answer.append(i)
        answer.append(0)
        answer.sort()
    else:    
        for i in range(-total, total+1):
            if cnt == num:
                if sum(answer) != total:
                    answer.remove(answer[0])
                    cnt -= 1
                else:
                    break            
            answer.append(i)
            cnt += 1
    
    return answer

print(solution(5, 15))