from collections import deque

n = int(input())
g = list([] for _ in range(10))

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    g[a].append(b)
    g[b].append(a)

que = deque()
que.append(1)
s = {1}
while que:
    v = que.popleft()
    for i in g[v]:
        if not i in s:
            que.append(i)
            s.add(i)
print(max(s))