h, w, x, y = map(int, input().split())
board = []
for i in range(h):
  board.append(list(input()))
cnt = 1
x -= 1
y -= 1
if x == 0:
    for i in range(1,h):
        if board[i][y] == "#":
            break
        else:
            cnt += 1
elif x == h-1:
    for i in range(x-1,-1,-1):
        if board[i][y] == "#":
            break
        else:
            cnt += 1
else:
    for i in range(x-1, -1, -1):
        if board[i][y] == "#":
            break
        else:
            cnt += 1
    for i in range(x+1, h):
        if board[i][y] == "#":
            break
        else:
            cnt += 1
if y == 0:
    for j in range(1,w):
        if board[x][j] == "#":
            break
        else:
            cnt += 1
elif y == w-1:
    for j in range(y-1, -1, -1):
        if board[x][j] == "#":
            break
        else:
            cnt += 1
else:
    for j in range(y-1, -1, -1):
        if board[x][j] == "#":
            break
        else:
            cnt += 1
    for j in range(y+1, w):
        if board[x][j] == "#":
            break
        else:
            cnt += 1
print(cnt)