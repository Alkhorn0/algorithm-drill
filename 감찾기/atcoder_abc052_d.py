n, a, b = map(int, input().split())
x = list(map(int, input().split()))
s = x[0]
ans = 0
for i in range(1, n):
    ans += min(b, a*(x[i]-s))
    s = x[i]

print(ans)