# sw 역량 테스트 준비 - 기초 
from collections import deque

s = int(input())
visited = [[-1]*(s+1) for _ in range(s+1)]

q = deque()
q.append((1, 0))
visited[1][0] = 0

while q:
    x, y = q.popleft()
    if visited[x][x] == -1:
        visited[x][x] = visited[x][y]+1
        q.append((x, x))
    if x+y <= s and visited[x+y][y] == -1:
        visited[x+y][y] = visited[x][y]+1
        q.append((x+y, y))
    if x-1 >= 0 and visited[x-1][y] == -1:
        visited[x-1][y] = visited[x][y] + 1
        q.append((x-1, y))

ans = -1
for i in range(s+1):
    if visited[s][i] != -1:
        if ans == -1 or ans > visited[s][i]:
            ans = visited[s][i]
print(ans)