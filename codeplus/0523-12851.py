# bfs
from collections import deque

n, k = map(int, input().split())
visited = [-1]*100001
q = deque()
q.append(n)
visited[n] = 0
cnt = 0
while q:
    x = q.popleft()
    if x == k:
        cnt += 1
    for i in [2*x, x+1, x-1]:
        if 0 <= i <= 100000:
            # 아예 방문한적 없거나, 시간이 동일하게 걸렸을 때 큐에 추가해줌
            if visited[i] == -1 or visited[i] >= visited[x]+1:
                q.append(i)
                visited[i] = visited[x]+1
print(visited[k])
print(cnt)