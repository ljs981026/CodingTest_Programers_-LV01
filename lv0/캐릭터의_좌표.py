def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    dy = [0,0,1,-1]
    dx = [-1,1,0,0]
    move = ['left','right','up','down']

    for k in keyinput:
        for m in range(len(move)):
            if k == move[m]:
                nx = x + dx[m]
                ny = y + dy[m]
        # print(y, -board[1]//2)
        if nx < -board[0]/2 or ny < -board[1]/2 or nx > board[0]/2 or ny > board[1]/2:
            continue
        x, y = nx, ny
    answer.append(x)
    answer.append(y)
    return answer

print(solution(["left", "right", "up", "right", "right"]))