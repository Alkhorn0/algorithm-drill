# 다시보기
from collections import deque
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
t = int(input())
for _ in range(t):
    n = int(input())
    now_x, now_y = map(int, input().split())
    aim_x, aim_y = map(int, input().split())
    d = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((now_x, now_y))
    d[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
    print(d[aim_x][aim_y])