# 그래프문제
def dfs(answer, graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            answer.append(i)
            dfs(answer, graph, i, visited)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
answer = []
visited = [False]*(n+1)
dfs(answer, graph, 1, visited)
print(len(answer))