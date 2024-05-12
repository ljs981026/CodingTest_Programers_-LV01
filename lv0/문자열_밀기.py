def solution(A, B):
    if A == B:
        return 0
    
    for i in range(len(A)):
        print(A[-1])
        A = A[-1] + A[:-1]
        if A == B:
            return i+1
    
    return -1

solution=lambda a,b:(b*2).find(a)

print(solution("hello","ohell"))
