# backtracking
# 다시보기
# 스도쿠: 9*9칸에서 가로, 세로, 3*3정사각형 안에서 겹치지 않게 1-9가 한 번씩 들어가는 퍼즐

# 3*3 정사각형 만드는 함수
def square(x, y):
    # (1~3행,4~6행,7~9행)*(1~3열 / 4~6열 / 7~9열)
    return (x//3)*3 + (y//3)

def go(z):
    # 탐색 끝
    if z == 81:
        for row in a:
            # 출력
            print(' '.join(map(str, row)))
        return True
    # 9*9행렬에 0-80까지의 번호를 붙여 탐색 
    # (0행 0열 == 0, 1행 1열 == 9, 9행 9열 == 80)
    x = z//n    # 값 z == x행 y열 표시
    y = z%n
    if a[x][y] != 0:
        return go(z+1)
    else:
        for i in range(1, 10):
            # 숫자 i가 그 자리에 들어갈 수 있는지 파악
            if c[x][i] == False and c2[y][i] == False and c3[square(x, y)][i] == False:
                # 숫자 대입 및 변경 갱신
                c[x][i] = c2[y][i] = c3[square(x, y)][i] = True
                a[x][y] = i
                # 계속 진행
                if go(z+1):
                    return True
                # 다른 경우도 찾기위해 원상복구
                a[x][y] = 0
                c[x][i] = c2[y][i] = c3[square(x, y)][i] = False
    return False

n = 9
a = [list(map(int, input().split())) for _ in range(n)]
# 2차원배열로 만들어 행, 열, 사각형내에 숫자가 있는 지 없는지를 파악
c = [[False]*10 for _ in range(n)]  # c[i][j] == True -> i행에 숫자 j 있음
c2 = [[False]*10 for _ in range(n)] # c[i][j] == True -> i열에 숫자 j 있음
c3 = [[False]*10 for _ in range(n)] # c[i][j] == True -> i번째 사각형에 숫자 j 있음
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            c[i][a[i][j]] = True
            c2[j][a[i][j]] = True
            c3[square(i, j)][a[i][j]] = True
go(0)