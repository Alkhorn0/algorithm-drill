# sw 역량 테스트 준비 - 기초 
def square(x, y):
    return (x//3)*3 + (y//3)

def go(z):
    if z == 81:
        for row in a:
            print(' '.join(map(str, row)))
        return True
    x = z//9
    y = z%9
    if a[x][y] != 0:
        return go(z+1)
    else:
        for i in range(1, 10):
            if check_row[x][i] == False and check_col[y][i] == False and check_square[square(x, y)][i] == False:
                check_row[x][i] = check_col[y][i] = check_square[square(x, y)][i] = True
                a[x][y] = i
                if go(z+1):
                    return True
                a[x][y] = 0
                check_row[x][i] = check_col[y][i] = check_square[square(x, y)][i] = False
    return False                

a = [list(map(int, input().split())) for _ in range(9)]
check_row = [[False]*10 for _ in range(9)]
check_col = [[False]*10 for _ in range(9)]
check_square = [[False]*10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if a[i][j] != 0:
            check_row[i][a[i][j]] = True
            check_col[j][a[i][j]] = True
            check_square[square(i, j)][a[i][j]] = True
go(0)