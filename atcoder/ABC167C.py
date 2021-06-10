n, m, x = map(int, input().split())
c = []
a = []
for _ in range(n):
    ci, *ai = list(map(int, input().split()))
    c.append(ci)
    a.append(ai)
ans = sum(c)+1
for i in range(1<<n):
    l = [0]*m
    cost = 0
    for j in range(n):
        if ((i>>j)&1):
            cost += c[j]
            for k in range(m):
                l[k] += a[j][k]
    
    ok = True
    for j in range(m):
        if l[j] < x:
            ok = False
    if ok:
        ans = min(ans, cost)
if ans == sum(c)+1:
    print(-1)
else:
    print(ans)