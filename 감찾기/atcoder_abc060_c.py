n, T = map(int, input().split())
t = list(map(int, input().split()))
ans = 0
re = 0
s = 0
for i in range(n):
    if s < t[i]:
        ans += (s-re)
        re = t[i]
    s = t[i]+T
    if i == n-1:
        ans += (s-re)

print(ans)