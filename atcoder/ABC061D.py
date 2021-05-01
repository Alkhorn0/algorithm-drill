# 벨만포드 (복습할 것)
n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]
INF = -float("inf")
dist = [INF]*n
dist[0] = 0

d_tmp = 0
for i in abc: # 같은게 두번 나오는 이유는 inf 의 경우를 찾아내기 위함
    dist[i[1]-1] = max(dist[i[1]-1], dist[i[0]-1]+i[2])

d_tmp = dist[-1]
for j in abc: # 위의 결과와 다른 dist 값이있으면 inf 가 됨 
    dist[j[1]-1] = max(dist[j[1]-1], dist[j[0]-1]+j[2])

print(dist[-1]) if d_tmp == dist[-1] else print("inf")