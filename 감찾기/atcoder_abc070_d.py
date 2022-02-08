import sys
sys.setrecursionlimit(100000000)

n = int(input())
g = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

dist = [-1 for _ in range((n+1))]

def dfs(cur, d):
    for n, n_dist in g[cur]:
        if dist[n] < 0:
            dist[n] = d+n_dist
            dfs(n, dist[n])

q, k = map(int, input().split())
dist[k] = 0
dfs(k, 0)
for i in range(q):
    x, y = map(int, input().split())
    print(dist[x] + dist[y])