# sw 역량 테스트 준비 - 기초 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1e7)

n, m = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)