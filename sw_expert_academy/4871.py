def DFS(s):
    visited[s] = True
    result = 0
    if s in graph:  # 연결된게 있으면
        for connect in graph[s]:
            if not visited[connect]:     #아직 미방문
                if connect == g:
                    return 1 
                elif not result:    # 결과가 안났으면 계속 탐색
                    result += DFS(connect)
    return result
T = int(input())
for t in range(1, T+1):
    v, e = map(int, input().split())
    graph = {}  # dictionary
    visited = [False] * (v+1)
    result = 0
    for _ in range(e):
        start, end = map(int, input().split())
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)

    s, g = map(int, input().split())
    print(f'#{t} {DFS(s)}')