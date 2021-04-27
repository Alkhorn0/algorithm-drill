# bfs 문제
from collections import deque 
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)

n, k = map(int, input().split())
visited = [0] * 100001
bfs()