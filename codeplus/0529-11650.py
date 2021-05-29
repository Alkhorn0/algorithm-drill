# sorting
import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x:x[1])
a.sort(key=lambda x:x[0])

for i in range(n):
    print(a[i][0],a[i][1])