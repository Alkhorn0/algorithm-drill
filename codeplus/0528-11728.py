# merge sort, 분할정복
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def merge(a, b):
    ans = [1e10]*(n+m)
    i, j, cnt = 0, 0, 0
    while i < n and j < m:
        if a[i] <= b[j]:
            ans[cnt] = a[i]
            i += 1
        else:
            ans[cnt] = b[j]
            j += 1
        cnt += 1
    
    while i < n:
        ans[cnt] = a[i]
        i += 1
        cnt += 1
    while j < m:
        ans[cnt] = b[j]
        j += 1
        cnt += 1
    return ans

print(' '.join(map(str, merge(a, b))))