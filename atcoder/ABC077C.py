# 이분탐색 문제
import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
ans = 0
for i in b: 
    a_cnt = bisect.bisect_left(a, i)
    c_cnt = bisect.bisect_right(c, i)
    ans += a_cnt*(n - c_cnt)
print(ans)