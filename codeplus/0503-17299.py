# 자료구조, 스택
n = int(input())
a = list(map(int, input().split()))
f = [0]*(max(a)+1)
s = []
ans = [0]*n
for i in a:
    f[i] += 1
for j in range(n):
    if not s:
        s.append(j)
    while s and f[a[s[-1]]] < f[a[j]]:
        ans[s.pop()] = a[j]
    s.append(j)
while s:
    ans[s.pop()] = -1
print(' '.join(map(str, ans)))