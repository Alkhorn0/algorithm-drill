def dfs(graph, v, visited, connect, cnt):
    visited[v] = True
    connect[v] = cnt

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, connect,cnt)

n, k, l = map(int, input().split())
road_connect = [0 for _ in range(n+1)]
train_connect = [0 for _ in range(n+1)]
road = [[] for _ in range(n+1)]
train = [[] for _ in range(n+1)]
visited_road = [False]*(n+1)
visited_train = [False]*(n+1)
for _ in range(k):                      #各頂点別、道路で連結した頂点を表す。
    p, q = map(int, input().split())
    road[p].append(q)
    road[q].append(p)
for _ in range(l):                      #各頂点別、鉄道で連結した頂点を表す。
    r, s = map(int, input().split())
    train[r].append(s)
    train[s].append(r)
cnt_road = 1
cnt_train = 1

for i in range(1, n+1):
    if not visited_road[i] and len(road[i]) != 0: 
        dfs(road, i, visited_road, road_connect, cnt_road)
        cnt_road += 1                   #連結されている道路の番号　
for j in range(1, n+1):
    if not visited_train[j] and len(train[j]) != 0:
        dfs(train, j, visited_train, train_connect, cnt_train)
        cnt_train += 1                  #連結されている鉄道の番号
status = []
for k in range(n+1):                    #道路の情報と鉄道の情報を合わせる
    status.append([road_connect[k], train_connect[k]])
answer = [0]*n
for a in range(1, n+1):
    for b in range(1, n+1):
        if 0 in status[a]:              #どちらかが0の場合、つながっていないのでその都市だけ数える
            answer[a-1] = 1
            break
        elif status[a] == status[b]:    #同じ連結情報を持った都市の数を数える
            answer[a-1] += 1
for ans in answer:
    print(ans, end=' ')