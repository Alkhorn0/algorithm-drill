# 그리디 , 풀이법 개선(시간초과)
n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
cranes.sort(reverse=True)
boxes.sort(reverse=True)
time = 0
if boxes[0] > cranes[0]:
    print(-1)
else:
    while boxes:
        time += 1
        for i in range(n):
            for j in range(len(boxes)):
                if cranes[i] >= boxes[j]:
                    boxes.remove(boxes[j])
                    break
    print(time)