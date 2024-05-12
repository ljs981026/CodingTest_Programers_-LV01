def solution(board):
    answer = 0
    bomb_l = []

    # 폭탄 위치 확인
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                bomb_l.append([i,j])    
                
    # 폭탄 주변 표시
    for i in bomb_l:
        if i[0] - 1 > -1:
            board[i[0]-1][i[1]] = 1
            # 왼 대각선
            if i[1] - 1 > -1:
                board[i[0]-1][i[1]-1] = 1
            # 오른 대각선
            if i[1]+1 < len(board):
                board[i[0]-1][i[1]+1] = 1                            
        # 중간 왼
        if i[1] - 1 > -1:
            board[i[0]][i[1]-1] = 1
        # 중간 오
        if i[1] + 1 < len(board):
            board[i[0]][i[1]+1] = 1
    
        # 아래
        if i[0]+1 < len(board):
            board[i[0]+1][i[1]] = 1
            # 왼 대각선
            if i[1]-1 > -1:
                board[i[0]+1][i[1]-1] = 1
            # 오른 대각선
            if i[1]+1 < len(board):
                board[i[0]+1][i[1]+1] = 1
    
    # 안전지대 카운트
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                answer += 1
    
    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
