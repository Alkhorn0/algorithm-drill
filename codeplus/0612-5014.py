from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [False]*(f+1)
dist = [1e10]*(f+1)
q = deque()
q.append(s)
dist[s] = 0
visited[s] = True
while q:
    v = q.popleft()
    if v+u <= f:
        if not visited[v+u]:
            dist[v+u] = dist[v]+1
            visited[v+u] = True
            q.append(v+u)
    if v-d > 0:
        if not visited[v-d]:
            dist[v-d] = dist[v]+1
            visited[v-d] = True
            q.append(v-d)
print(dist[g] if dist[g] != 1e10 else 'use the stairs')