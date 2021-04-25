# 푸는 중
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
road = {}
for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                print(-1)
                exit()
            elif graph[a][b] == graph[a][k] + graph[k][b] and a > b and k != a and k!= b:
                road[graph[a][k]] = [a, k]
                road[graph[b][k]] = [b, k]
print(road)