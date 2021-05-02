# greedy 
# 문제해설 : n개의 센서들을 k개의 구간으로 나누는 것과 동일
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

if k >= n:  # 집중국 수가 더 많거나 같으면 센서수 만큼 집중국을 설치하면 됨
    print(0)
    sys.exit()

dist = []   # 인접한 센서 사이의 거리
for i in range(1, n):
    dist.append(sensor[i] - sensor[i-1])

dist.sort(reverse=True) # 수신가능 영역을 줄이기 위해선 센서사이의 거리가 긴 부분은 끊어가야함
for _ in range(k-1):  # k개 구간으로 나누기 위해선 k-1번 끊으면 됨
    dist.pop(0)
print(sum(dist))