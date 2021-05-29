# sorting, hashing
import sys
input = sys.stdin.readline

n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())
a.sort()
ans = a[0]
ans_cnt = 1
cnt = 1
for i in range(1, n):
    if a[i] == a[i-1]:
        cnt += 1
    else:
        cnt = 1
    if ans_cnt < cnt:
        ans_cnt = cnt
        ans = a[i]
print(ans)