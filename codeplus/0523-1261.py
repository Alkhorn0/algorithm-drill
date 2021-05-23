from collections import deque

m, n = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
d = [[-1]*m for _ in range(n)]
q = deque()
q.append((0, 0))
d[0][0] = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        # 벽이 있는 경우와 없는경우의 차이를 나타냄
        if 0 <= nx < n and 0 <= ny < m:
            if d[nx][ny] == -1:
                # 벽이 없는 경우 벽을 부술 필요가 없기때문에 그대로 대입
                # 더 먼저 bfs에 넣고 돌리기 전에 q의 앞쪽에 추가되게 해야함
                if a[nx][ny] == 0:
                    d[nx][ny] = d[x][y]
                    q.appendleft((nx, ny))
                # 위와 반대
                else:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
print(d[n-1][m-1])