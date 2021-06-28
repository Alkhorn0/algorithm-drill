# sw 역량 테스트 준비 - 기초 
from collections import deque

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    a = [list(map(int, input().split())) for _ in range(h)]
    d = [[0]*w for _ in range(h)]
    q = deque()
    cnt = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == 1 and d[i][j] == 0:
                cnt += 1
                q.append((i, j))
                d[i][j] = cnt
                while q:
                    x, y = q.popleft()
                    for k in range(8):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < h and 0 <= ny < w:
                            if a[nx][ny] == 1 and d[nx][ny] == 0:
                                d[nx][ny] = d[x][y]
                                q.append((nx, ny))
    print(cnt)