def backtracking(x, y):
    #　시계방향 (우, 하, 좌, 상)
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    global isPath

    if maze[y][x] == 3:
        isPath = 1
        return
    
    visited.append((x, y))
    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]

        # 방문 x, 범위 내, 벽(1)이 x
        if (nextX, nextY) not in visited and (0<=nextX<n and 0<=nextY<n) and maze[nextY][nextX] != 1:
            backtracking(nextX, nextY)

def findStart():
    for y in range(n):
        for x in range(n):
            if maze[y][x] == 2:
                return x, y 

T = int(input())

for t in range(1, T+1):
    # 미로의 크기
    n = int(input())
    maze = [[int(i) for i in input()] for _ in range(n)]

    # 시작점 찾기
    startX, startY = findStart()

    visited = []
    isPath = 0
    backtracking(startX, startY)
    #print(visited)
    print(f'#{t} {isPath}')