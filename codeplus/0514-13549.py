from collections import deque
MAX = 200000
visited = [False]*MAX
dist = [-1]*MAX
n, k = map(int, input().split())
visited[n] = True
dist[n] = 0
q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x*2 < MAX and visited[x*2] == False:
        q.appendleft(x*2)
        visited[x*2] = True
        dist[x*2] = dist[x]
    if x-1 >= 0 and visited[x-1] == False:
        q.append(x-1)
        visited[x-1] = True
        dist[x-1] = dist[x]+1
    if x+1 < MAX and visited[x+1] == False:
        q.append(x+1)
        visited[x+1] = True
        dist[x+1] = dist[x]+1
print(dist[k])