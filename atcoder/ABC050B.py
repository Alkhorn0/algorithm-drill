n = int(input())
t = list(map(int, input().split()))
m = int(input())
s = sum(t)
for _ in range(m):
    temp = s
    pi, xi = map(int, input().split())
    temp -= t[pi-1]
    temp += xi
    print(temp)