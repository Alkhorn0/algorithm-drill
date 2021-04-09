n = int(input())
mass = []
for __ in range(n):
    l = list(map(int,input().split()))
    mass.append(l)
for i in range(len(mass)):
    cnt = 1
    for j in range(0, len(mass)):
        if mass[i][0] < mass[j][0] and mass[i][1] < mass[j][1]:
            cnt += 1
    print(cnt,end=" ")