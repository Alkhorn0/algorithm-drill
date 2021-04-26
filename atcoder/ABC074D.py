# 워셜 플로이드
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for i in range(n):
    graph[i][i] = int(1e11)

for a in range(n):
    for b in range(a+1, n):
        m = int(1e11)
        for k in range(n):
            m = min(m, graph[a][k] + graph[k][b])
        
        if graph[a][b] > m:
            print(-1)
            exit()
        elif graph[a][b] < m:
            answer += graph[a][b]

print(answer)