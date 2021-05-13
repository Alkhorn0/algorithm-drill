# 다시보기(3종류중 한종류만 사용해서)
n, m = map(int, input().split())
edges = [] # 간선 리스트
arr = [[False]*n for _ in range(n)]   # 인접행렬
g = [[] for _ in range(n)]  # 인접 리스트
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))
    edges.append((b, a))
    arr[a][b] = arr[b][a] = True
    g[a].append(b)
    g[b].append(a)
m *= 2
for i in range(m):
    for j in range(m):
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not arr[B][C]:
            continue
        for E in g[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            exit()
print(0)