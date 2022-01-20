import sys
sys.setrecursionlimit(10**8)

n = int(input())
a = [0]
for _ in range(n):
    a.append(int(input()))
visited = [0]*(n+1)
cnt = 1
def dfs(i, cnt):
    if visited[i]:
        return
    visited[i] = cnt
    dfs(a[i], cnt+1)

dfs(1, cnt)

print(visited[2]-1 if visited[2] else -1)