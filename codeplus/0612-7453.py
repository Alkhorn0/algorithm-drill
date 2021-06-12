# 다시보기
# brute force
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
temp = [list(map(int, input().split())) for _ in range(n)]
a, b, c, d = zip(*temp)
first = []
second = []

for i in range(n):
    for j in range(n):
        first.append(a[i]+b[j])
        second.append(c[i]+d[j])
c = Counter(second)
ans = 0
for num in first:
    ans += c[-num]
print(ans)
