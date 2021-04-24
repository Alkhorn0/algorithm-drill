# 재귀문제
def recursive(n, board):
    standard = board[0][0]
    judge = 0
    global blue
    global white
    for y in range(n):
        for x in range(n):
            if standard != board[y][x]:
                judge = 1
                break
        if judge == 1:
            break
    if judge == 1:
        n //= 2
        board1, board2, board3, board4 = [], [], [], []
        for i in range(n):
            board1.append(board[i][:n])
            board2.append(board[i][n:])
            board3.append(board[i+n][:n])
            board4.append(board[i+n][n:])
        recursive(n, board1)
        recursive(n, board2)
        recursive(n, board3)
        recursive(n, board4)
    else:
        if board[0][0] == 1:
            blue += 1
        else:
            white += 1

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
blue = 0
white = 0

recursive(n, board)
print(white, blue)
