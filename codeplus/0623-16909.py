# 다시보기
import sys
input = sys.stdin.readline

def calc(n):
    return n*(n+1)//2

n = int(input().rstrip())
a = [0] + list(map(int, input().rstrip().split()))
ans = 0
lg = [0]*(n+1)
rg = [n+1]*(n+1)
ls = [0]*(n+1)
rs = [n+1]*(n+1)
sg, ss = [], []
sg.append((1, a[1]))
ss.append((1, a[1]))
for i in range(2, n+1):
    while sg != [] and a[i] > sg[-1][1]:
        rg[sg[-1][0]] = i
        sg.pop()
    sg.append((i, a[i]))
    while ss != [] and a[i] <= ss[-1][1]:
        rs[ss[-1][0]] = i
        ss.pop()
    ss.append((i, a[i]))

sg, ss = [], []
sg.append((n, a[n]))
ss.append((n, a[n]))
for i in range(n-1, 0):
    while sg != [] and a[i] > sg[-1][1]:
        lg[sg[-1][0]] = i
        sg.pop()
    sg.append((i, a[i]))
    while ss != [] and a[i] < ss[-1][1]:
        ls[ss[-1][0]] = i
        ss.pop()
    ss.append((i, a[i]))

for i in range(1, n+1):
    l = min(i, lg[i]+1)
    r = max(i, rg[i]-1)
    length = r-l+1
    ans += (calc(length) - calc(r-i) - calc(i-l))*a[i]
    print(ans)
for i in range(1, n+1):
    l = min(i, ls[i]+1)
    r = max(i, rs[i]-1)
    length = r-l+1
    ans -= (calc(length) - calc(r-i) - calc(i-l))*a[i]
    print(ans)
print(ans)