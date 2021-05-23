from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

h , w = map(int, input().split())
s = [list(input()) for _ in range(h)]
white = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            white += 1

q = deque()
q.append((0, 0))

inf = 10**10
d = [[inf]*w for _ in range(h)]
d[0][0] = 1
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if s[nx][ny] == '#' or d[nx][ny] != inf:
            continue
        d[nx][ny] = d[x][y] + 1
        q.append((nx, ny))

if d[h-1][w-1] == inf:
    print(-1)
else:
    print(white-d[h-1][w-1])