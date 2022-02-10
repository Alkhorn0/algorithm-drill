n = int(input())
p = list(map(int, input().split()))
l = []
for i in range(n):
    if i+1 == p[i]:
        l.append(0)
    else:
        l.append(1)
l.append(True)
ans = 0
for i in range(n):
    if not (l[i]):
        ans += 1
        l[i] = True
        l[i+1] = True
print(ans)