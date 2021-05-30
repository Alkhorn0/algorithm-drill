# greedy, bitmask
# 해설에는 뒤집는 구현을 하지만 파이썬의 경우 뒤집으면 시간초과가 뜸
# 때문에 직접 뒤집지는 않고 행을 뒤집는 시행의 경우의 수에 대해 결정 후 
# 열마다 뒤집는다고 가정하는 경우에는 H의 갯수(뒤집으면 T가되므로), 
# 뒤집지 않는 경우에는 T의 갯수를 세서 작은 수를 더함
# 비트마스크를 이용해 뒤집는 시행을 나타낸다
import sys
input = sys.stdin.readline

n = int(input())
a = [input() for _ in range(n)]
ans = n*n
for k in range(1<<n):
    sum = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
    # k = 0-> 행을 뒤집지 않음, 1<<j = 0 -> i행의 j열을 뒤집지 않음
            # k&(1<<j) -> a[i][j]가 뒤집혀있는가 -> 1=yes,0=no
            if k & (1<<j):
                if a[i][j] == 'H':
                    cnt += 1
            else:
                if a[i][j] == 'T':
                    cnt += 1
    # 이 경우 더 작은 수만 더하는 것은 t의 갯수가 더 작은 경우를 얻기 위함
        sum += min(cnt, n-cnt)
    if ans > sum:
        ans = sum
print(ans)