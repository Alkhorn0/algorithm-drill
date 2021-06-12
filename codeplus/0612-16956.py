from collections import deque

r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
for i in range(r):
    for j in range(c):
        if a[i][j] == 'S':
            q.append((i, j))

possible = True
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if a[nx][ny] == 'W':
                possible = False
if not possible:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if a[i][j] == '.':
                a[i][j] = 'D'
        print(''.join(map(str, a[i])))