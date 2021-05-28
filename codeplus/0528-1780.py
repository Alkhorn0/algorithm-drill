# 분할정복, recursion
# 종이 1장에서 시작해 모든칸의 숫자가 같은지 확인, 
# 아닐 경우 9등분의 반복

import sys
sys.setrecursionlimit(100000)

# 종이 1장의 모든칸에 같은 수인지 판정
def same(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 가장 왼쪽 위의 숫자 기준 
            if a[x][y] != a[i][j]:
                return False
    return True 

# 종이 한장에 모든 수가 같은 수인지 판정하는 함수 
# + 아닐경우 종이를 9등분
def solve(x, y, n):
    # 같은 경우 종이 한장이 -1, 0, 1로 통일 되었으므로 
    # 맞는 곳에 1더해줌
    if same(x, y, n):
        cnt[a[x][y]+1] += 1
        return
    # 아닌경우 종이 한장을 9등분
    # (종이 한장크기 n*n -> n/3*n/3)
    m = n//3
    for i in range(3):
        for j in range(3):
            # 전화패드(1->9까지 확인, 재귀)
            solve(x+i*m, y+j*m, m)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# -1,0,1의 갯수를 세는 용도
cnt = [0]*3
solve(0, 0, n)
for i in range(3):
    print(cnt[i])