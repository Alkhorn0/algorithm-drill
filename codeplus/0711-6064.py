# sw 역량 테스트 준비 - 기초 
t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    i = x
    ans = -1
    while i < m*n:
        if i%n == y:
            ans = i+1
            break
        i += m
    print(ans)
    