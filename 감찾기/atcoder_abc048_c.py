n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

y = a[0]
for i in a[1:]:
    y += i
    diff = 0
    if y > x:
        diff = (y-x)
        ans += diff
    y = (i-diff) if i-diff >= 0 else 0

print(ans)