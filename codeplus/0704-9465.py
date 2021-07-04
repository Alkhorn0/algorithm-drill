# sw 역량 테스트 준비 - 기초 
t = int(input())
for _ in range(t):
    n = int(input())
    d = [[0]*2 for _ in range(n+1)]
    a = [list(map(int, input().split())) for _ in range(2)]
    d[1][0] = a[0][0]
    d[1][1] = a[1][0]
    d[2][0] = a[0][1] + a[1][0]
    d[2][1] = a[0][0] + a[1][1]
    for i in range(3, n+1):
        d[i][0] = max(d[i-2][1], d[i-1][1]) + a[0][i-1]
        d[i][1] = max(d[i-2][0], d[i-1][0]) + a[1][i-1]
    print(max(d[n]))