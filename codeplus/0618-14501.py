# sw 역량 테스트 준비 - 기초 
n = int(input())
t = []
p = []
ans = 0
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)
def go(day, income, index):
    global ans
    if day == n+1:
        if ans < income:
            ans = income
        return
    if day > n+1:
        return
    go(day+t[index], income+p[index], index+t[index])
    go(day+1, income, index+1)
go(1, 0, 0)
print(ans)