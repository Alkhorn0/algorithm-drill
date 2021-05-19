# brute force, recursive
def go(step, x1, y1, x2, y2):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 조작이 10번 이상 넘어가면 실패
    if step == 11:
        return -1
    # 동전 1과 동전 2가 떨어졋는지 아닌지 기록
    fall1 = False
    fall2 = False
    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
        fall1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
        fall2 = True
    # 둘다 떨어지면 실패
    if fall1 and fall2:
        return -1
    # 하나만 떨어진 경우는 성공 -> 조작횟수 반환
    if fall1 or fall2:
        return step
    ans = -1
    for k in range(4):
        nx1, ny1 = x1+dx[k], y1+dy[k]
        nx2, ny2 = x2+dx[k], y2+dy[k]
        # 이동하려는 곳이 벽이면 이동 불가
        if 0 <= nx1 < n and 0 <= ny1 < m and board[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if 0 <= nx2 < n and 0 <= ny2 < m and board[nx2][ny2] == '#':
            nx2, ny2 = x2, y2
        temp = go(step+1, nx1, ny1, nx2, ny2)
        # 조작시 답이 안나오는 경우 -> 패스
        if temp == -1:
            continue
        # 진행중이거나 최소 조작횟수를 표시하는 문제이므로 갱신이 필요한 경우
        if ans == -1 or ans > temp:
            ans = temp
    return ans

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
x1 = y1 = x2 = y2 = -1
for i in range(n):
    for j in range(m):
        # 동전의 위치탐색
        if board[i][j] == 'o':
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j
            # 동전이 있는 칸에도 이동가능 하므로 
            # 동전의 위치를 알았으면 조작중에는 빈칸으로 여겨도 됨
            board[i][j] = '.'
print(go(0, x1, y1, x2, y2))