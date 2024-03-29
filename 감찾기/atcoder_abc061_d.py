n, m = map(int, input().split())
abc = list(list(map(int, input().split())) for _ in range(m))
INF = -float('inf')
dist = [INF]*n
dist[0] = 0

# 최장경로 갱신
for i in abc:
    dist[i[1]-1] = max(dist[i[1]-1], dist[i[0]-1]+i[2])
#print(dist)

# 폐로의 존재 확인 -> 있으면 변동사항이 있음
d_tmp = dist[-1]
for j in abc:
    dist[j[1]-1] = max(dist[j[1]-1], dist[j[0]-1]+j[2])
#print(dist)

print(dist[-1]) if d_tmp == dist[-1] else print('inf')

