def go(day, income):
    global ans
    if day == n:
        ans = max(ans, income)
        return
    elif day > n:
        return
    go(day+1, income)
    go(day+t[day], income+p[day])

n = int(input())
t, p = [], []
ans = 0
for _ in range(n):
    t_i, p_i = map(int, input().split())
    t.append(t_i)
    p.append(p_i)
go(0, 0)
print(ans)