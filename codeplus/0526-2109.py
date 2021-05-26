# greedy, heap
# d일까지 와서 강의를 하면 p원을 받으니까 (p,d) = (2,1),(10,2),(10,2) 가 주어진 경우,
# (10,2),(10,2)를 골라야 한다 -> 날짜에대해 오름차순으로 받아서 
# x일을 기준으로 x일까지 오면 되는 강연중에서 가장 보수가 높은 일을 x개까지 
# 남기고 더하면 된다 -> x개 까지 남기고 더하는 부분에서 우선순위를 매기기 위해 최소힙 활용

import sys, heapq
input = sys.stdin.readline

n = int(input())
r = []
for _ in range(n):
    r.append(list(map(int, input().split())))
# 강연에 대한 정보를 받아 날짜기준으로 오름차순 정렬 
r.sort(key=lambda x: x[1])
tmp = []
for i in r:
    # 보수에대한 정보만 추가한다 
    heapq.heappush(tmp, i[0])
    # len(tmp) = 기준이 되는 x일 일을 받을 수 있는 갯수, i[1] = 강연을 하기 위해 오면 되는 날짜
    # 즉, 1일까지 오면 되는 일이 여러개일 경우 그때 할 수 있는건 가장 큰 보수를 주는 일 뿐이다
    # 다른예로 7일까지 오면 되는 일이 7개가 있다면 1일에 1개씩 모두 받을 수 있다는 말
    # 이를 len(tmp)로 나타냄 또한 최소heap을 사용하여 작은 것 부터 빼내어, 큰 수만 남길 수 있도록 한다
    if len(tmp) > i[1]:
        heapq.heappop(tmp)
print(sum(tmp))