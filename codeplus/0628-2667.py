# sw 역량 테스트 준비 - 기초 
from collections import deque

n = int(input())
a = [list(input()) for _ in range(n)]
d = [[0]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == '1' and d[i][j] == 0:
            cnt += 1
            q = deque()
            q.append((i, j))
            d[i][j] = cnt
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if d[nx][ny] == 0 and a[nx][ny] == '1':
                            d[nx][ny] = d[x][y]
                            q.append((nx, ny))

print(cnt)
ans = [0]*cnt
for i in range(n):
    for j in range(n):
        if d[i][j] != 0:
            ans[d[i][j]-1] += 1
ans.sort()
print('\n'.join(map(str, ans)))