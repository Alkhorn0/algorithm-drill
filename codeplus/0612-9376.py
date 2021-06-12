# 다시보기
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(a, x, y):
    h = len(a)
    w = len(a[0])
    dist = [[-1]*w for _ in range(h)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and dist[nx][ny] == -1 and a[nx][ny] != '*':
                if a[nx][ny] == '#':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
    return dist

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    a = ['.'+input()+'.' for _ in range(h)]
    h += 2
    w += 2
    a = ['.'*w] + a + ['.'*w]
    d0 = bfs(a, 0, 0)
    x1 = y1 = x2 = y2 = -1
    for i in range(h):
        for j in range(w):
            if a[i][j] == '$':
                if x1 == -1:
                    x1, y1 = i, j
                else:
                    x2, y2 = i, j
    d1 = bfs(a, x1, y1)
    d2 = bfs(a, x2, y2)
    ans = h*w

    for i in range(h):
        for j in range(w):
            if a[i][j] == '*':
                continue
            if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
                continue
            temp = d0[i][j] + d1[i][j] + d2[i][j]
            if a[i][j] == '#':
                temp -= 2
            ans = min(ans, temp)
    print(ans)
