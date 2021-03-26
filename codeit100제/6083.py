import sys
r, g, b = map(int, sys.stdin.readline().split())
s = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            s += 1
print(s)