# greedy
import sys
input = sys.stdin.readline
n = int(input())
number = [0] * n
for i in range(n):
    number[i] = int(input())
number.sort()
ans = 0
for j in range(n):
    ans += abs(number[j]-(j+1))
print(ans)