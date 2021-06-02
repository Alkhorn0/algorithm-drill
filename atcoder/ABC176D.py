from collections import deque

h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
s = [list(input()) for _ in range(h)]

visited = [[-1]*w for _ in range(h)]
noq = deque()
noq.append((ch-1, cw-1))
oneq = deque()
visited[ch-1][cw-1] = 0

while noq:
    x, y = noq.popleft()
    oneq.append((x, y))
    for (i, j) in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
        nx = x+i
        ny = y+j
        if 0 <= nx < h and 0 <= ny < w:
            if visited[nx][ny] == -1 and s[nx][ny] == '.':
                visited[nx][ny] = visited[x][y]
                noq.append((nx, ny))
    
    if len(noq) == 0:
        while oneq:
            x2, y2 = oneq.popleft()
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if (i, j) in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                        continue
                    dx, dy = x2+i, y2+j
                    if 0 <= dx < h and 0 <= dy < w:
                        if visited[dx][dy] == -1 and s[dx][dy] == '.':
                            visited[dx][dy] = visited[x2][y2] + 1
                            noq.append((dx, dy))
    
print(visited)
print(visited[dh-1][dw-1])