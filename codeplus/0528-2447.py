# 다시보기

n = int(input())
a = [[' ']*n for _ in range(n)]
def go(a, x, y, n, color):
    if color == ' ':
        for i in range(x, x+n):
            for j in range(y, y+n):
                a[i][j] = ' '
    else:
        if n == 1:
            a[x][y] = '*'
        else:
            m = n//3
            for i in range(3):
                for j in range(3):
                    if i == 1 and j == 1:
                        color = ' '
                    else:
                        color = '*'
                    go(a, x+m*i, y+m*j, m, color)
go(a, 0, 0, n, '*')
for i in range(n):
    print(''.join(map(str, a[i])))