# sorting
import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    name, k, e, m = input().split()
    k, e, m = int(k), int(e), int(m)
    a.append([name, k, e, m])
a.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in a:
    print(i[0])