# bfs 문제
from collections import deque
def bfs(m, n, box):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.append([i, j])
    while q:
        point = q.popleft()
        x = point[1]
        y = point[0]
        for i in range(4):
            x_i = x + dx[i]
            y_i = y + dy[i]
            if 0 <= x_i < m and 0 <= y_i < n:
                if box[y_i][x_i] == 0:
                    q.append([y_i, x_i])
                    box[y_i][x_i] = box[y][x] + 1

    

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
ans = 0
bfs(m, n, box)
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()
        ans = max(box[i][j], ans)
print(ans-1)