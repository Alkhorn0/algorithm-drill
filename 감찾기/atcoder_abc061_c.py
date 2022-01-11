n, k = map(int, input().split())
array = []
cnt = 0
ans = 0
t = False
for i in range(n):
    ai, bi = map(int, input().split())
    array.append((ai, bi))

array.sort(key=lambda x: x[0])

for a, b in array:
    cnt += b
    if cnt >= k:
        ans = a
        break
print(ans)