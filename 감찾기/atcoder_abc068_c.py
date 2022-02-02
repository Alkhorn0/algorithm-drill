n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

judge = False
for i in g[1]:
    for j in g[i]:
        if j == n:
            judge = True


if judge:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')