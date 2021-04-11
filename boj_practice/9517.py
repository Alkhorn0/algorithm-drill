# 구현문제
k = int(input())
n = int(input())
time = 210
answer = []
for __ in range(n):
    answer.append(list(input().split()))

for i in range(n):
    time -= int(answer[i][0])
    if time <= 0:
        break
    if answer[i][1] == "T":
        k += 1
        if k > 8:
            k = 1
    
print(k)