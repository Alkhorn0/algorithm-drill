# 다시보기
# n*(2n-1)이 전부 *로 채워진 그림에서부터 시작

# 삼각형으로 출력할 부분 안쪽의 빈칸 생성목적
def go(a, x, y, n, color):
    if color == ' ':
        m = 2*n-1
        # 역삼각형모양으로 빈칸을 만듬
        # n = 6의 경우 a[i][j] -> (3, 3)~(3, 7)/(4, 4)~(4, 6)/(5, 5)
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
                # n이 3인경우 (1,2)(삼각형의 중앙부분) 빈칸
                go(a, x+1, y, 1, ' ')
            else:
                # 가운데 부분 역삼각형모양으로 빈칸
                go(a, x+m, y-m+1, m, ' ')


n = int(input())
# 받을때 n*2n 으로 받음
a = [['*']*(2*n) for _ in range(n)]
go(a, 0, n-1, n, '*')
# 비교용
#for i in range(n):
    #print(''.join(map(str, a[i])))
for i in range(n):
    for j in range(n-i-1):
        # 윤곽부분 빈칸 n = 3 의 경우
        # (0,0),(0,1),(1,0)
        a[i][j] = ' '
        # (0,3),(0,4),(1,4)
        a[i][2*n-j-2] = ' '
    # (0,5),(1,5),(2,5) -> 끝부분
    a[i][2*n-1] = ' '

for i in range(n):
    print(''.join(map(str, a[i])))