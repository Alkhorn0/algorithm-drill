# 다시보기
# brute force, recursive
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False]*m for _ in range(n)]
# ㅜ를 제외한 다른 4개의 테트로미노는 연속 한다고 볼 수 있음(재귀로 더해줌)
# 한변과 맞닿은 면으로 나아가는 형태는 모두포함(원래 갔던 곳으로 돌아오는 것 배제해야함)
def go(x, y, sum, cnt):
    if cnt == 4:
        global ans
        if ans < sum:
            ans = sum
        return
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    # 원래 갔던 곳으로 돌아오는 것 배제
    if c[x][y]:
        return
    c[x][y] = True
    for k in range(4):
        go(x+dx[k], y+dy[k], sum+a[x][y], cnt+1)
    c[x][y] = False
ans = 0
# ㅜ모양의 파생형은 따로 더해준다
for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)
        if j+2 < m:
            temp = a[i][j] + a[i][j+1] + a[i][j+2]
            if i - 1 >= 0:
                temp2 = temp + a[i-1][j+1]  # ㅗ모양 
                if ans < temp2:
                    ans = temp2
            if i + 1 < n:
                temp2 = temp + a[i+1][j+1]  # ㅜ모양
                if ans < temp2:
                    ans = temp2
        if i+2 < n:
            temp = a[i][j] + a[i+1][j] + a[i+2][j]  
            if j+1 < m:
                temp2 = temp + a[i+1][j+1]  # ㅏ모양
                if ans < temp2:
                    ans = temp2
            if j-1 >= 0:
                temp2 = temp + a[i+1][j-1]  # ㅓ모양
                if ans < temp2:
                    ans = temp2
print(ans)