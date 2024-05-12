def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y = 0, 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    direction = 0
    for i in range(1,(n*n)+1):
        answer[y][x] = i
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if nx >= n or nx < 0 or ny >= n or ny < 0 or answer[ny][nx] != 0:
            direction = (direction + 1) % 4         
            nx = x + dx[direction]
            ny = y + dy[direction]       
        x, y = nx, ny            
        
    return answer

print(solution(5))