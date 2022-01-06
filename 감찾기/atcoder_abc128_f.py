n = int(input())
s = list(map(int, input().split()))
ans = 0

for c in range(1, n):
    tmp = 0
    for k in range(1, n):
        if k*c >= n-1: break
        i = k*c
        j = n-1-k*c
        if i == j: break
        a = n-1-i
        if a <= c: break
        tmp += s[i] + s[j]
        ans = max(ans, tmp)
        if i + c == j: break

print(ans)