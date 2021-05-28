# 다시보기

def go(a, x, y, n, color):
    if color == ' ':
        m = 2*n-1
        for i in range(x, x+n):
            for j in range(m):
                a[i][j+i-x+y] = ' '
            m -= 2
    elif color == '*':
        if n != 1:
            m = n//2
            go(a, x, y, m, '*')
            go(a, x+m, y-m, m, '*')
            go(a, x+m, y+m, m, '*')
            if n == 3:
                go(a, x+1, y, 1, ' ')
            else:
                go(a, x+m, y-m+1, m, ' ')

n = int(input())
a = [['*']*(2*n) for _ in range(n)]
go(a, 0, n-1, n, '*')
for i in range(n):
    for j in range(n-i-1):
        a[i][j] = ' '
        a[i][2*n-j-2] = ' '
    a[i][2*n-1] = ' '

for i in range(n):
    print(''.join(map(str, a[i])))