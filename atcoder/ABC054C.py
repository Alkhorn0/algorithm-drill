n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
answer = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, cnt):
    cnt += 1
    count = 0
    if cnt == n:
        answer.append(1)
        return 
    stack = graph[v]
    visited[v] = True
    for i in stack:
        if visited[i]:
            continue
        dfs(i, cnt)
    visited[v] = False
dfs(1, 0)
print(len(answer))