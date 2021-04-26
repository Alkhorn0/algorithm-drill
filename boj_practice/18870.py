import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
x = list(sorted(set(l)))
x = {x[i]:i for i in range(len(x))}
for j in l:
    print(x[j], end=' ')