from collections import deque, defaultdict

n, k, l = map(int, input().split())
road = [[] for _ in range(n)]
train = [[] for _ in range(n)]
connect_road = [0] * n
connect_train = [0] * n
for _ in range(k):
    p, q = map(int, input().split())
    road[p-1].append(q-1)
    road[q-1].append(p-1)
for _ in range(l):
    r, s = map(int, input().split())
    train[r-1].append(s-1)
    train[s-1].append(r-1)

print(road)
print(train)

def bfs(start, now, graph, connect):
    q = deque([start])
    connect[start] = now
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not connect[i]:
                connect[i] = now
                q.append(i)

now1, now2 = 0, 0
for i in range(n):
    if not road[i]:
        now1 += 1
        bfs(i, now1, road, connect_road)
    
    if not train[i]:
        now2 += 1
        bfs(i, now2, train, connect_train)
d = defaultdict(int)
for d1,d2 in zip(connect_road, connect_train):
    d[(d1, d2)] += 1
print(connect_road)
print(connect_train)
print(d)
for d1, d2 in zip(connect_road, connect_train):
    print(d[(d1,d2)])