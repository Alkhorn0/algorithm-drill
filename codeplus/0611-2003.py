# 브루트포스
n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    temp = a[i]
    if temp == m:
        ans += 1
        continue
    for j in range(i+1, n):
        temp += a[j]
        if temp == m:
            ans += 1
            break
        elif temp > m:
            break
print(ans)