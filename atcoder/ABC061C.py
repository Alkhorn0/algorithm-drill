n, k = map(int, input().split())
l = []
ans = 0
for _ in range(n):
    a_i, b_i = map(int, input().split())
    l.append((a_i, b_i))
l.sort()

for a, b in l:
    k -= b
    if k <= 0:
        ans = a
        break
print(ans)