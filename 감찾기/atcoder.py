n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())
k = m-1
cmp = t[k]
ans = []

for i in range(n-1, -1, -1):
    if cmp == s[i]:
        ans.append('Yes')
        k -= 1
        cmp = t[k]
    else:
        ans.append('No')

ans = ans[::-1]
for a in ans:
    print(a)