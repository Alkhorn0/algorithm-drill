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
    # 위의 시행에서 a혹은 b의 원소가 먼저 전부 배치되면 동작
    # 즉, 아래 두개의 while문 중 동작하는 것은 1개뿐
    # a혹은 b에 남아 있는 원소 전부 ans로 대입
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