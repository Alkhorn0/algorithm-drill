# sw 역량 테스트 준비 - 기초 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, a, alpha):
    r = len(a)
    c = len(a[0])
    ans = 0
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if  0 <= nx < r and 0 <= ny < c:
            if alpha[ord(a[nx][ny])-ord('A')] == False:
                alpha[ord(a[nx][ny])-ord('A')] = True
                temp = move(nx, ny, a, alpha)
                if ans < temp:
                    ans = temp
                alpha[ord(a[nx][ny])-ord('A')] = False
    return ans+1


r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
alpha = [False]*26
alpha[ord(a[0][0])-ord('A')] = True
print(move(0, 0, a, alpha))