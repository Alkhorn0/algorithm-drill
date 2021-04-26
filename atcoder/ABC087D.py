from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    l, r, d = map(int, input().split())
    graph[l].append([r, d])
    graph[r].append([l, -d])

point = [None] * (n+1)

for i in range(1, n+1):
    if point[i] != None:
        continue
    point[i] = 0
    d = deque()
    d.append(i)
    while d:
        start = d.popleft()
        for end, distance in graph[start]:
            if point[end] != None:
                if point[end] != point[start] + distance:
                    print('No')
                    exit()
                continue
            point[end] = point[start] + distance
            d.append(end)
print('Yes')

