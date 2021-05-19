# backtracking, recursive, brute force
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move(x, y, board, alpha, cnt, r, c):
    global ans
    if cnt > ans:
        ans = cnt
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if alpha[ord(board[nx][ny])-ord('A')] == False:
                alpha[ord(board[nx][ny])-ord('A')] = True
                move(nx, ny, board, alpha, cnt+1, r, c)
                alpha[ord(board[nx][ny])-ord('A')] = False

r, c = map(int, input().split())
board = [input() for _ in range(r)]
alpha = [False]*26
alpha[ord(board[0][0])-ord('A')] = True
ans = 1
move(0, 0, board, alpha, 1, r, c)
print(ans)