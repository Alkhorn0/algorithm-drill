# 다시보기, 트리, bfs
from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
a = [[] for _ in range(v+1)]
for _ in range(v):
    c = list(map(int, input().split()))
    for e in range(1, len(c)-2, 2):
        a[c[0]].append((c[e], c[e + 1]))

def bfs(start):
    visited = [-1] * (v+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    dist = [0, 0]

    while q:
        x = q.popleft()
        for e, w in a[x]:
            if visited[e] == -1:
                visited[e] = visited[x] + w
                q.append(e)
                if dist[0] < visited[e]:
                    dist = visited[e], e
    return dist
# 트리의 지름-> 임의의 노드에서 가장 멀리있는 노드를 구한 후
# 해당노드에서 한번더 탐색하여 가장 멀리 있는 노드를 구한 값
ans, node = bfs(1)
ans, node = bfs(node)
print(ans)