# 다시보기
n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(0)
    exit()

ans = -1
for d1 in range(-1, 1+1):
    for d2 in range(-1, 1+1):
        change = 0
        if d1 != 0:
            change += 1
        if d2 != 0:
            change += 1
        a0 = a[0] + d1
        diff = (a[1] + d2) - a0
        ok = True
        an = a0 + diff
        for i in range(2, n):
            an += diff
            if a[i] == an:
                continue
            if a[i] - 1 == an:
                change += 1
            elif a[i] + 1 == an:
                change += 1
            else:
                ok = False
                break
        if ok:
            if ans == -1 or ans > change:
                ans = change
print(ans)



'''
#메모리초과
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())
B = list(map(int, input().split()))
inf = 1e10
if n == 1:
    print(0)
    exit()

def go(index, cnt, B):
    if index == len(B):
        r = B[1]-B[0]
        ok = True
        for i in range(1, len(B)-1):
            if B[i+1] - B[i] != r:
                ok = False
                return inf
        if ok:
            return cnt
    ans = len(B)
    b = B[:]
    p = go(index+1, cnt, B)
    b[index] += 1
    p2 = go(index+1, cnt+1, b)
    b[index] -= 2
    p3 = go(index+1, cnt+1, b)
    return min(p, p2, p3)
ans = go(0, 0, B)
print(ans if ans != inf else -1)
'''