maze = [list(map(int, input().split())) for i in range(10)]

x, y = 1, 1
maze[1][1] = 9

while True:
    # 오른쪽이 0
    if maze[x][y + 1] == 0:
        y += 1
        maze[x][y] = 9
    # 오른쪽이 1
    elif maze[x][y + 1] == 1:
        if maze[x + 1][y] == 1:
            break
        elif maze[x + 1][y] == 2:
            x += 1
            maze[x][y] = 9
            break
        else: 
            x += 1
            maze[x][y] = 9
    # 오른쪽이 2
    else:
        y += 1
        maze[x][y] = 9
        break

for i in range(10):
    for j in range(10):
        print(maze[i][j], end=' ')
    print()
