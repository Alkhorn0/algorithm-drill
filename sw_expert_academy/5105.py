def IsSafe(y, x):
    return (0<=y<n and 0<=x<n) and (maze[y][x] == 0 or maze[y][x] == 3)

def BFS(start_y, start_x):
    global D_result
    Q.append((start_y, start_x))
    visited.append((start_y, start_x))

    while Q:
        start_y, start_x = Q.pop(0)
        for dir in range(4):
            newY = start_y + dy[dir]
            newX = start_x + dx[dir]
            if IsSafe(newY, newX) and (newY, newX) not in visited:
                Q.append((newY, newX))
                visited.append((newY, newX))
                Distance[newY][newX] = Distance[start_y][start_x] + 1
                if maze[newY][newX] == 3:
                    D_result = Distance[newY][newX] - 1
                    return 

T = int(input())
for t in range(1, T+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if maze[y][x] == 2:
                start_y, start_x = y, x
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    D_result = 0
    Q = []
    Distance = [[0]*n for _ in range(n)]
    BFS(start_y, start_x)
    print(Distance)
    print(f'#{t} {D_result}')