# 한 번 더 보기
m = 9
dx = [0, 1]
dy = [1, 0]

def convert(l):
    return (ord(l[0])-ord('A'), ord(l[1])-ord('1'))

def square(x, y):
    return (x//3)*3 + (y//3)

def check(x, y, num, what):
    c[x][num] = what
    c2[y][num] = what
    c3[square(x, y)][num] = what

def check_range(x, y):
    return 0 <= x < m and 0 <= y < m

def can(x, y, num):
    return not c[x][num] and not c2[y][num] and not c3[square(x, y)][num]

def go(z):
    if z == 81:
        for i in range(m):
            print(''.join(map(str, a[i])))
        return True
    x = z//m
    y = z%m
    if a[x][y] != 0:
        return go(z+1)
    else:
        for k in range(2):
            nx, ny = x+dx[k], y+dy[k]
            if not check_range(nx, ny):
                continue
            if a[nx][ny] != 0:
                continue
            for i in range(1, 10):
                for j in range(1, 10):
                    if i == j:
                        continue
                    if domino[i][j]:
                        continue
                    if can(x, y, i) and can(nx, ny, j):
                        check(x, y, i, True)
                        check(nx, ny, j, True)
                        domino[i][j] = domino[j][i] = True
                        a[x][y] = i
                        a[nx][ny] = j
                        if go(z+1):
                            return True
                        check(x, y, i, False)
                        check(nx, ny, j, False)
                        domino[i][j] = domino[j][i] = False
                        a[x][y] = 0
                        a[nx][ny] = 0
    return False

T = 1
while True:
    c = [[False]*10 for _ in range(10)]
    c2 = [[False]*10 for _ in range(10)]
    c3 = [[False]*10 for _ in range(10)]
    domino = [[False]*10 for _ in range(10)]
    a = [[0]*9 for _ in range(9)]
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        u,lu,v,lv = input().split()
        u = int(u)
        v = int(v)
        x1, y1 = convert(lu)
        x2, y2 = convert(lv)
        a[x1][y1] = u
        a[x2][y2] = v
        domino[u][v] = domino[v][u] = True
        check(x1, y1, u, True)
        check(x2, y2, v, True)
    temp = input().split()
    for i in range(1, 10):
        l = temp[i-1]
        x, y = convert(l)
        a[x][y] = i
        check(x, y, i, True)
    print(f'Puzzle {T}')
    go(0)
    T += 1