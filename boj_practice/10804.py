# 시뮬레이션 문제
l = [i for i in range(1,21)]
for _ in range(10):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d = (b-a+1)//2
    for i in range(d):
        l[a+i], l[b-i] = l[b-i], l[a+i]
for j in l:
    print(j, end=' ')
