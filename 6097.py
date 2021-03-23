h, w = map(int, input().split())
board = [[0] * w for i in range(h)]

n = int(input())
for __ in range(n):
    l, d, x, y = map(int,input().split())
    if d == 0:
        for j in range(l):
            board[x - 1][y + j - 1] = 1
    else:
        for j in range(l):
            board[x + j - 1][y - 1] = 1

for i in range(h):
    for j in range(w):
        print(board[i][j], end=' ')
    print()