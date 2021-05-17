# 다른방법 찾아보기(출력부분)
from collections import deque, Counter
from functools import reduce

n = int(input())
a = [list(map(int, input())) for _ in range(n)]
group = [[0]*n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0
def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    group[x][y] = cnt
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n  and 0 <= ny < n:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx, ny))
                    group[nx][ny] = cnt

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)

ans = reduce(lambda x, y : x+y, group)
ans = [x for x in ans if x > 0]
ans = sorted(list(Counter(ans).values()))
print(cnt)
print('\n'.join(map(str, ans)))