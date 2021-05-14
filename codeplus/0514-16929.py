# 다시보기
n, m = map(int, input().split())
a = [input() for _ in range(n)]
dist = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def go(x, y, cnt, color):
    if visited[x][y]:
        if cnt - dist[x][y] >= 4:
            return True
        else:
            return False
    visited[x][y] = True
    dist[x][y] = cnt
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == color:
                if go(nx, ny, cnt+1, color):
                    return True
    return False
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        dist = [[0]*m for _ in range(n)]
        if go(i, j, 1, a[i][j]):
            print('Yes')
            exit()
print('No')