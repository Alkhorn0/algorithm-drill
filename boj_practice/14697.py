a, b, c, n = map(int, input().split())

cnt = 0
for i in range(n//a+1):
    for j in range(n//b+1):
        for k in range(n//c+1):
            if a*i + b*j + c*k == n:
                cnt += 1

if cnt == 0:
    print(0)
else:
    print(1)