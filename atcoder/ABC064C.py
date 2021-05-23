n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
b = 0
for i in a:
    cnt = (b+i) - x
    if cnt > 0:
        ans += cnt
        i -= cnt
    b = i
print(ans)