# 다시보기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    g = [[] for _ in range(v+1)]
    part = [0]*(v+1)
    for _ in range(e):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    def dfs(v, c):
        part[v] = c
        for i in g[v]:
            if part[i] == 0:
                if not dfs(i, 3-c):
                    return False
            elif part[i] == part[v]:
                return False
        return True
    
    ans = True
    for i in range(1, v+1):
        if part[i] == 0:
            if not dfs(i, 1):
                ans = False
    print('YES' if ans else 'NO')