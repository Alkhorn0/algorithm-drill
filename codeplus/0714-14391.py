# sw 역량 테스트 준비 - 기초 
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
ans = 0
for k in range(1<<(n*m)):
    s = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            t = i*m+j
            if (k&(1<<t)) == 0:
                cur = cur*10 + a[i][j]
            else:
                s += cur
                cur = 0
        s += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            t = i*m+j
            if (k&(1<<t)) != 0:
                cur = cur*10 + a[i][j]
            else:
                s += cur
                cur = 0
        s += cur
    ans = max(ans, s)
print(ans)