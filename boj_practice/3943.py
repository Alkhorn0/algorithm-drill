# 시뮬레이션 문제
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    heilstone = []
    while True:
        if 1 in heilstone:
            break
        heilstone.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3+1
    print(max(heilstone))
