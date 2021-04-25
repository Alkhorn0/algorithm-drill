n, m = map(int, input().split())
info = {}
visited = [0 for _ in range(n+1)]
for i in range(1, n+1):
    info[i] = 0
judge = False
for _ in range(m):
    l, r, d = map(int, input().split())
    visited[l] = 1
    if visited[r] == 1 and info[r] != info[l]+d:
        judge = True
    else:    
        info[r] = info[l]+d
        visited[r] = 1
if judge:
    print('No')
else:
    print('Yes')
