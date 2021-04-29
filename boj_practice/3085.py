# 구현
import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(str, input())) for _ in range(n)]

result = 0

def check(board):
    cnt = 0
    for i in range(n):
        cnt_row = 1
        cnt_col = 1
        for j in range(n-1):       # 순회하며 체크 
            if board[i][j] == board[i][j+1]:    # 행 체크
                cnt_row += 1
            else:
                cnt = max(cnt, cnt_row)
                cnt_row = 1
            
            if board[j][i] == board[j+1][i]:    # 열 체크
                cnt_col += 1
            else:
                cnt = max(cnt, cnt_col)
                cnt_col = 1
        cnt = max(cnt, cnt_row, cnt_col)
    return cnt

for i in range(n):
    for j in range(n-1):
        if board[i][j] != board[i][j+1]:
            # 인접 교환(같은 행)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            result = max(result, check(board))
            # 원상 복구
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if board[j][i] != board[j+1][i]:
            # 인접 교환(같은 열)
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            result = max(result, check(board))
            # 원상복구
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(result)