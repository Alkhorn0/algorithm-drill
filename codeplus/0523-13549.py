# bfs
from collections import deque

n, k = map(int, input().split())
visited = [-1]*100001
q = deque()
q.append(n)
visited[n] = 0
while q:
    x = q.popleft()
    if x == k:
        break
    for i in [2*x, x+1, x-1]:
        if 0 <= i <= 100000:
            # 순간이동의 경우 걸리는 시간이 0이므로 우선적으로 처리해야함
            if i == 2*x and visited[i] == -1:
                q.appendleft(i)
                visited[i] = visited[x]
            elif (i == x+1 or i == x-1) and visited[i] == -1:
                q.append(i)
                visited[i] = visited[x]+1
print(visited[k])