n = int(input())
time = sorted(list(map(int,input().split())))

max_time = 0
for i in range(n):
    max_time += time[i] * (n - i)

print(max_time)

