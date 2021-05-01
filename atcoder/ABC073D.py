# 워셜 플로이드 & 순열(복습 필요)
import sys
input = sys.stdin.readline
from itertools import permutations

def warshall_floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])

n, m, R = map(int, input().split())
r = list(map(int, input().split()))
d = [[10**10]*n for _ in range(n)]

for i in range(n):
    d[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c

warshall_floyd()
ans = 10**10

for p in permutations(r):
    now = p[0]-1
    possible = 0
    for i in range(1, R):
        possible += d[now][p[i]-1]
        now = p[i]-1
    ans = min(ans, possible)

print(ans)