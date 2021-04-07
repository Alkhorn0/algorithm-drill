n = int(input())
l = []
for __ in range(n):
    start, end = map(int, input().split())
    l.append([start, end])
l = sorted(l, key=lambda time: time[0]) #시작시간 기준으로 정렬
l = sorted(l, key=lambda time: time[1]) #종료시간 기준으로 정렬
last = 0
cnt = 0
for start,end in l:
    if start >= last:
        cnt += 1
        last = end

print(cnt)