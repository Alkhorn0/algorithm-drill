n = int(input())
s = []
for _ in range(n):
    s.append(input())
m = int(input())
t = []
for _ in range(m):
    t.append(input())
check = list(set(s))
ans = 0
for i in check:
    cnt = 0
    for j in s:
        if i == j:
            cnt += 1
    for k in t:
        if i == k:
            cnt -= 1
    ans = max(cnt, ans)
print(ans)