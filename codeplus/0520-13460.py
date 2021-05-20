# 다시보기
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
LIMIT = 10

# 각 칸의 상태를 나타냄, 이동가능 여부, 구멍인지 여부, 좌표
class Result:
    def __init__(self, moved, hole, x, y):
        self.moved = moved
        self.hole = hole
        self.x = x
        self.y = y

def gen(k):
    a = [0]*LIMIT
    for i in range(LIMIT):
        # 2진수 -> 4진수/ 00 -> 0/ 01-> 1/ 10-> 2/ 11-> 3
        a[i] = (k&3)
        # 4진수로 만들며 2진수 2자리를 하나로 합침
        k >>= 2
    # k(2진수) -> a(4진수)
    return a

# 행한 이동이 무의미한지 유의미한지 판단 
# (무의미한 이동 -> 같은방향으로 연속 2번이동 & 반대방향으로 연속해서 이동)
def valid(dirs):
    l = len(dirs)
    for i in range(l-1):
        if dirs[i] == 0 and dirs[i+1] == 1:
            return False
        if dirs[i] == 1 and dirs[i+1] == 0:
            return False
        if dirs[i] == 2 and dirs[i+1] == 3:
            return False
        if dirs[i] == 3 and dirs[i+1] == 2:
            return False
        if dirs[i] == dirs[i+1]:
            return False
    return True

# a-> 보드의 상태/ k-> 조작 방법/ x,y -> 이동하고자하는 구슬의 좌표
def simulate(a, k, x, y):
    n = len(a)
    m = len(a[0])
    if a[x][y] == '.':
        # 각 보드의 칸에는 좌표외에도 담아야 될 정보가 많아 class로 만들어 대응
        return Result(False, False, x, y)
    moved = False
    while True:
        nx, ny = x+dx[k], y+dy[k]
        # 보드의 밖으로는 나갈 수 없음
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return Result(moved, False, x, y)
        # 이동할 위치
        ch = a[nx][ny]
        # 벽인 경우에는 이동 불가
        if ch == '#':
            return Result(moved, False, x, y)
        # 구슬끼리는 겹치지 못함, 이동 불가
        elif ch in 'RB':
            return Result(moved, False, x, y)
        # 빈칸으로는 이동가능, 이동한 칸은 빈칸과 위치가 바뀐다고 여길 수 있음,
        # 좌표이동, 이동가능표시
        elif ch == '.':
            a[x][y], a[nx][ny] = a[nx][ny], a[x][y]
            x, y = nx, ny
            moved = True
        # 구멍의 경우 빈칸으로 여기되 위치가 바뀌지는 않음, 
        # 이동 가능, 빈칸 표시
        elif ch == 'O':
            a[x][y] = '.'
            moved = True
            return Result(moved, True, x, y)

# 보드의 상태 a와 이동방법 dirs일때 문제의 조건을 만족하는지 판단
def check(a, dirs):
    n = len(a)
    m = len(a[0])
    hx, hy = 0, 0
    rx, ry = 0, 0
    bx, by = 0, 0

    # 구멍과, 구슬들의 위치 파악
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'O':
                hx, hy = i, j
            elif a[i][j] == 'R':
                rx, ry = i, j
            elif a[i][j] == 'B':
                bx, by = i, j
    
    # 조작횟수 기록
    cnt = 0
    for k in dirs:
        cnt += 1
        # hole1 -> 빨간 구슬이 hole에 가는 경우/ hole2 -> 파란구슬이 hole에 가는 경우
        hole1 = hole2 = False
        while True:
            # 빨간 구슬에대한 이동 시뮬레이션
            p1 = simulate(a, k, rx, ry)
            # 빨간 구슬의 좌표
            rx, ry = p1.x, p1.y
            # 파란 구슬에 대한 이동 시뮬레이션
            p2 = simulate(a, k, bx, by)
            # 파란구슬의 좌표
            bx, by = p2.x, p2.y

            # 두 구슬다 이동못하게 된 경우 -> 조작 종료
            if not p1.moved and not p2.moved:
                break
            # 빨간 구슬이 구멍의 위치에있다 = 빨간구슬이 나갔다
            if p1.hole:
                hole1 = True
            # 파란 구슬이 구멍의 위치에있다 = 파란구슬이 나갔다
            if p2.hole:
                hole2 = True
        # 파란구슬이 나가면 조작은 실패이기 때문에 파란구슬만 우선적으로 검사
        if hole2:
            return -1
        # 파란구슬이 나가지 않고 빨간구슬이 나가면 조작 성공이므로 조작횟수 반환 
        if hole1:
            return cnt
    return -1

n, m = map(int, input().split())
board = [input() for _ in range(n)]
ans = -1
# 가능한 이동방향은 4방향이므로 2진수인 비트마스크로 표현을위해선 LIMIT*2를 해준다
for k in range(1 << (LIMIT*2)):
    # gen의 기능 -> 4진수로 만듬
    dirs = gen(k)
    # 무의미한 이동은 삭제
    if not valid(dirs):
        continue
    # 이동했을때의 보드의 상태
    a = [list(row) for row in board]
    # 문제의 조건을 만족하는 결과를 내는지 판단
    cur = check(a, dirs)
    if cur == -1:
        continue
    if ans == -1 or ans > cur:
        ans = cur

print(ans)