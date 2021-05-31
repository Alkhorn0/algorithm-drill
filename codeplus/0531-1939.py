import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
f1, f2 = map(int, input().split())

def dfs(v, mid):
    visited[v] = True
    if v == f2:
        return True
    for i, w in g[v]:
        if not visited[i]:
            if mid <= w:
                if dfs(i, mid):
                    return True
    return False

ans = 0
left = 1
right = 1000000000
while left <= right:
    mid = (left+right)//2
    visited = [False]*(n+1)
    if dfs(f1, mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)

