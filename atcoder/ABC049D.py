n, k, l = map(int, input().split())
cities = [1 for _ in range(n)]
road = []
train = []
for _ in range(k):
    road.append(list(map(int, input().split())))
for _ in range(l):
    train.append(list(map(int, input().split())))
for i in range(n):
    city_number = i+1
    road_connect_list = []
    connect = city_number
    for j in range(k):
        if connect == road[j][0]:
            connect = road[j][1]
            road_connect_list.append(connect)
        elif connect == road[j][1]:
            connect = road[j][0]
            road_connect_list.append(connect)
        else:
            continue
    train_connect_list = []
    connect = city_number
    for h in range(l):
        if connect == road[h][0]:
            connect = road[h][1]
            train_connect_list.append(connect)
        elif connect == road[h][1]:
            connect = road[h][0]
            train_connect_list.append(connect)
    for o in train_connect_list:
        if o in road_connect_list:
            cities[i] += 1
    print(city_number, road_connect_list, train_connect_list)
for i in range(n):
    print(cities[i],end=' ')