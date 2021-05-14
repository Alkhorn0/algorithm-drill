from collections import deque

n, k = map(int, input().split())
visited = [0]*100001
q = deque()
q.append(n)
cnt = 0
while q:
    x = q.popleft()
    if x == k:
        print(visited[x])
        break
    for i in [x-1, x+1, 2*x]:
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = visited[x]+1
            q.append(i)
