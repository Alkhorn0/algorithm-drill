# sw 역량 테스트 준비 - 기초 
from collections import deque

n, k = map(int, input().split())
visited = [-1]*100001
q = deque()
q.append(n)
visited[n] = 0

while q:
    x = q.popleft()
    for i in [x-1, x+1, 2*x]:
        if i < 0 or i > 100000:
            continue
        if visited[i] != -1:
            continue
        visited[i] = visited[x]+1
        if visited[k] != -1:
            print(visited[k])
            exit()
        q.append(i)