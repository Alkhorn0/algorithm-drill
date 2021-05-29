# sorting
import sys
input = sys.stdin.readline

n = int(input())
a = [0]*10001
for _ in range(n):
    k = int(input())
    a[k] += 1

for i in range(10001):
    if a[i] == 0:
        continue
    for j in range(a[i]):
        print(i)