# 다시보기
T = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    a = [list(input()) for _ in range(n)]
    cnt = 0
    def go(x, y, cnt):
        ans = -1
        if cnt == 0:
            return 0
        def ok(x, y):
            return 0<= x < n and 0<= y < m
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            while ok(nx, ny) and a[nx][ny] == '.':
                a[nx][ny] = '#'
                cnt -= 1
                nx += dx[i]
                ny += dy[i]
            nx -= dx[i]
            ny -= dy[i]
            if not (x == nx and y == ny):
                temp = go(nx, ny, cnt)
                if temp != -1:
                    if ans == -1 or ans > temp+1:
                        ans = temp+1
            while not (x == nx and y == ny):
                a[nx][ny] = '.'
                cnt += 1
                nx -= dx[i]
                ny -= dy[i]
        return ans

    for i in range(n):
        for j in range(m):
            if a[i][j] == '.':
                cnt += 1
    ans = -1
    for i in range(n):
        for j in range(m):
            if a[i][j] == '.':
                a[i][j] = '#'
                temp = go(i, j, cnt-1)
                if temp != -1:
                    if ans == -1 or ans > temp:
                        ans = temp
                a[i][j] = '.'
    print(f'Case {T}: {ans}')
    T += 1
