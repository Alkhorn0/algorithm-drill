mod = 10**9+7
n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

xx = 0
yy = 0
for k in range(n):
    xx += (2*k-n+1)*x[k] % mod
for k in range(m):
    yy += (2*k-m+1)*y[k] % mod

print(xx*yy%mod)