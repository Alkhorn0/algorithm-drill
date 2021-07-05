# sw 역량 테스트 준비 - 기초 
n = int(input())
a = list(map(int, input().split()))
d = [0]*n
v = [-1]*n

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[i] < d[j]+1:
            d[i] = d[j]+1
            v[i] = j
p = 0
for k in range(n):
    if d[p] < d[k]:
        p = k
print(d[p])
def go(p):
    if p == -1:
        return
    go(v[p])
    print(a[p], end=' ')
go(p)
print()