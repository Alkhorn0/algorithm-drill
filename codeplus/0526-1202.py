# greedy, heap
# 그리디적인 생각보다는 최소힙, 최대힙의 사용처 및 활용능력이 중요한 듯
# python은 최소힙만을 제공하므로 최대힙으로 사용시엔 절댓값을 넣어 가장 큰 수 -> 가장 작은 수로 하여 사용가능(혹은 우선순위를 포함시킨다)
# 가방의 크기가 작은 가방부터 담을 수 있는 최대가치의 보석을 담는것 -> greedy적 사고
# 구현 -> 보석에 대한 데이터 입력을 받을 때 최소힙 사용 -> 무게 기준으로 정렬(오름차순) 
# -> 가방에 넣을 수 있는 보석중 가장 가치가 큰 보석을 우선적으로 넣을때 최대 힙 사용
import sys
import heapq
input = sys.stdin.readline

# 보석을 받을때 최소힙으로 받음 (무게를 기준으로 오름차순 정렬)
n, k = map(int, input().split())
j = []
for _ in range(n):
    heapq.heappush(j, list(map(int, input().split())))
b = []
for _ in range(k):
    b.append(int(input()))
b.sort()

answer = 0
# 가방에 들어갈 보석들 후보군(가치를 기준으로 내림차순 (최대힙))
tmp = []
for bag in b:
    # 가방에 들어갈 수 있는 보석들 대입
    while j and bag >= j[0][0]:
        heapq.heappush(tmp, -heapq.heappop(j)[1])
    # 가방에 넣을 보석이 있으면 한개 빼서 원래값으로 돌려 더해줌
    if tmp:
        answer -= heapq.heappop(tmp)
    # 보석보다 가방의 수가 더 많으면 나머지는 멈춤
    elif not j:
        break
print(answer)