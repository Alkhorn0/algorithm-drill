# 다시보기

n = int(input())
a = [[' ']*n for _ in range(n)]
def go(a, x, y, n, color):
    # 규칙의 확장을 위한 부분으로 전체를 9등분 했을때,
    # 가장 가운데 (1,1) 부분을 빈칸으로 만들어야 하는 규칙
    # 받은 n의 크기가 전체의 크기
    if color == ' ':
        for i in range(x, x+n):
            for j in range(y, y+n):
                a[i][j] = ' '
    else:
        if n == 1:
            a[x][y] = '*'
        else:
            m = n//3
            # 가장 작은 3*3의 형태로 나누어 확장시켜 간다
            # 이 경우 (1,1)의 위치가 빈칸 이를 재귀함수 형태로 호출
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