# dfs 문제
def dfs(v, visited, graph):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == True:
            continue
        dfs(i,visited,graph)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
answer = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for v in range(1,n+1):
    if not visited[v]:
        dfs(v, visited, graph)
        answer += 1
print(answer)