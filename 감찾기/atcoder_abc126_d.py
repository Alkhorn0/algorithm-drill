import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [0]*(n+1)

def dfs(v, lst=-1):
    for to, length in graph[v]:
        if to == lst:
            continue
        dist[to] = dist[v] + length
        dfs(to, v)

dfs(1)
for d in dist[1:]:
    print(d % 2)    # 흑백을 칠한것은 2로 나눈 나머지면 같아짐