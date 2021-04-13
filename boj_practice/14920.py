# 시뮬레이션 문제
c = int(input())
n = 1
while c != 1:
    if c % 2 == 0:
        c = c//2
    else:
        c = 3*c+1
    n += 1
print(n)