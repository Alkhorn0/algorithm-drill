n, m = map(int, input().split())
d = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1

for ans in d[1:]:
    print(ans)