# 그리디
import sys
input = sys.stdin.readline
n = int(input())
answer = 0
l = [0 for _ in range(n)]
for i in range(n):
    l[i] = int(input())
for j in range(n-1,0,-1):
    if l[j] <= l[j-1]:
        answer += l[j-1]-l[j]+1
        l[j-1] = l[j-1] - (l[j-1] - l[j]) - 1
print(answer)
