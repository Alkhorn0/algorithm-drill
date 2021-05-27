# 다시보기
n, m, k = map(int, input().split())
if n < m+k-1 or n > m*k:
    print(-1)
    exit()
a = [i for i in range(1, n+1)]
g = [0, k]
n -= k
m -= 1
gs = 0
r = 0
if m != 0:
    gs = n // m
    r = n % m
for i in range(m):
    v = g[-1]+gs
    if r > 0:
        v += 1
        r -= 1
    g.append(v)
ans = []
for i in range(len(g)-1):
    start = g[i]
    end = g[i+1]-1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
print(' '.join(map(str, a)))    