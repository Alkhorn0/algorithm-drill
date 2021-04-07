n, m = map(int, input().split())
board = []
for __ in range(n):
    board.append(input())

min_paint = 64

w_board = ["WBWBWBWB",
           "BWBWBWBW",
           "WBWBWBWB",
           "BWBWBWBW",
           "WBWBWBWB",
           "BWBWBWBW",
           "WBWBWBWB",
           "BWBWBWBW"]

b_board = ["BWBWBWBW",
           "WBWBWBWB",
           "BWBWBWBW",
           "WBWBWBWB",
           "BWBWBWBW",
           "WBWBWBWB",
           "BWBWBWBW",
           "WBWBWBWB"]

def compare(w_board, b_board, board):
    w_cnt = 0
    b_cnt = 0
    for i in range(8):
        for j in range(8):
            if w_board[i][j] != board[i][j]:
                w_cnt += 1
            if b_board[i][j] != board[i][j]:
                b_cnt += 1
    return min(w_cnt, b_cnt)

for x in range(n-7):
    for y in range(m-7):
        cutting = []
        for z in range(8):
            cutting.append(board[x+z][y:y+8])
        paint = compare(w_board, b_board, cutting)
        min_paint = min(min_paint,paint)
print(min_paint)