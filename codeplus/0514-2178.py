from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
g = [[0]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False]*m for _ in range(n)]

q = deque()
q.append((0, 0))
visited[0][0] = True
g[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                g[nx][ny] = g[x][y] + 1
                visited[nx][ny] = True

print(g[n-1][m-1])